from datetime import date, timedelta, timezone

from django.conf import settings
import stripe
from django.contrib.auth import get_user_model
User = get_user_model()
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import VendorProfileForm, VendorSignupForm
from django.contrib.auth.decorators import user_passes_test
from .models import VendorProfile, VendorImage,CATEGORY_CHOICES
from django.core.mail import send_mail


# ----------------- EMAIL HELPER -----------------
def send_email_to_user_and_admin(subject, message, user_email, fail_silently=False):
    admin_email = "godwinsenwin@gmail.com"  # admin email
    send_mail(
        subject=subject,
        message=message,
        from_email='no-reply@yourdomain.com',
        recipient_list=[user_email, admin_email],  # send to both
        fail_silently=fail_silently,
    )



# ----------------- SIGNUP -----------------
stripe.api_key = settings.STRIPE_SECRET_KEY
def signup_view(request):
    if request.method == "POST":
        form = VendorSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.status = 'pending'
            user.save()
            form.save_m2m()

            # Count free vendors
            free_count = VendorProfile.objects.filter(subscription_type='free').count()

            if free_count < 50:
                VendorProfile.objects.create(
                    user=user,
                    subscription_type='free',
                    subscription_expiry=date.today() + timedelta(days=365)
                )
            else:
                VendorProfile.objects.create(user=user, subscription_type='paid')

            # Send email to user + admin
            send_email_to_user_and_admin(
                subject="Registration Received – Pending Approval",
                message=(
                    f"Dear {user.username},\n\n"
                    "Thank you for registering with I Do In Greece. "
                    "Your account has been successfully created and is pending review.\n\n"
                    "Once approved by the admin, you will receive a confirmation email "
                    "with further instructions to update your profile and gallery.\n\n"
                    "Warm regards,\n"
                    "The I Do In Greece Team"
                ),
                user_email=user.email,
                fail_silently=False
            )

            messages.success(request, "Your account has been created, waiting for admin approval.")
            return redirect('login')
    else:
        form = VendorSignupForm()

    return render(request, "accounts/signup.html", {"form": form})



# ----------------- LOGIN -----------------
def custom_login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            if user.status == 'approved':
                login(request, user)
                return redirect('dashboard')
            elif user.status == 'pending':
                messages.error(request, "Your account is pending approval")
            else:
                messages.error(request, "Your account has been rejected")
        else:
            messages.error(request, "Invalid credentials, do you have an account.")
    return render(request, 'accounts/login.html')


# ----------------- LOGOUT -----------------
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


# ----------------- EDIT PROFILE -----------------
@login_required
def edit_profile(request):
    profile, created = VendorProfile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = VendorProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("dashboard")
    else:
        form = VendorProfileForm(instance=profile)
    return render(request, "accounts/edit_profile.html", {"form": form})



# ----------------- UPLOAD GALLERY IMAGE -----------------

@login_required
def upload_gallery_image(request):
    profile, created = VendorProfile.objects.get_or_create(user=request.user)

    if request.user.status != "approved":
        return JsonResponse({"error": "Account not approved"}, status=403)

    if profile.gallery.count() >= 5:
        return JsonResponse({"error": "Gallery full"}, status=400)
    if request.method == "POST":
        image = request.FILES.get("image")
        if image:
            new_image = VendorImage.objects.create(vendor=profile, image=image)

            # Notify admin only
            send_mail(
                subject="Action Required: New Gallery Image Uploaded by Vendor",
                message=(
                    f"Hello Admin,\n\n"
                    f"A new gallery image has been uploaded by the vendor '{request.user.username}'.\n\n"
                    f"Vendor Details:\n"
                    "Please review the image in the admin dashboard and take the necessary action "
                    "(approve or reject) to ensure it meets the platform standards.\n\n"
                    "Quick Actions:\n"
                    "1. Log in to the admin dashboard.\n"
                    "2. Navigate to 'Gallery Reviews'.\n"
                    "3. Approve or reject the newly uploaded image.\n\n"
                    "Thank you for keeping the platform content professional and up-to-date.\n\n"
                    "Best regards,\n"
                    "I Do In Greece Team"
                ),
                from_email="no-reply@yourdomain.com",
                recipient_list=["godwinsenwin@gmail.com"],  # admin email
                fail_silently=False,
            )
            return JsonResponse({"success": True})
        
    return JsonResponse({"error": "No image uploaded"}, status=400)



# ----------------- VENDOR DIRECTORY -----------------
from django.db.models import Count, Q
def vendor_directory(request):
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')

    vendor_list = VendorProfile.objects.annotate(
        approved_images=Count('gallery', filter=Q(gallery__status='approved'))
    ).filter(
        user__status='approved',
        approved_images__gt=0,
        user__is_superuser=False
    )

    if search_query:
        vendor_list = vendor_list.filter(
            Q(business_name__icontains=search_query) |
            Q(location__icontains=search_query)
        )

    if category_filter:
        vendor_list = vendor_list.filter(category=category_filter)

    vendor_list = vendor_list.order_by('-id')

    paginator = Paginator(vendor_list, 3)  # 6 per page
    page_number = request.GET.get('page')
    vendors = paginator.get_page(page_number)

    context = {
        "vendors": vendors,
        "search_query": search_query,
        "category_filter": category_filter,
        "categories": CATEGORY_CHOICES,  # <-- pass choices here
    }
    return render(request, "accounts/vendor_directory.html", context)
def vendor_profile_detail(request, user_id):
    vendor = get_object_or_404(VendorProfile, user__id=user_id)
    gallery = vendor.gallery.filter(status='approved')
    return render(request, "accounts/vendor_profile_detail.html", {"vendor": vendor, "gallery": gallery})



# ----------------- DASHBOARD -----------------
@login_required
def dashboard(request):
    profile = None
    gallery = VendorImage.objects.none()

    if request.user.is_vendor:
        try:
            profile = request.user.vendorprofile
            gallery = profile.gallery.all()

            required_fields = ['business_name', 'bio', 'location']
            incomplete = any(not getattr(profile, field) for field in required_fields)
            if incomplete:
                messages.warning(request, "Please complete your profile before accessing the dashboard.")
                return redirect('edit_profile')
        except VendorProfile.DoesNotExist:
            messages.warning(request, "Please complete your profile first.")
            return redirect('edit_profile')

    user_info = {
        "username": request.user.username,
        "email": request.user.email,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "date_joined": request.user.date_joined,
        "is_vendor": request.user.is_vendor,
        "status": request.user.status if request.user.is_vendor else None,
    }

    return render(request, "accounts/dashboard.html", {"profile": profile, "gallery": gallery, "user_info": user_info})

def dashboard_directory(request):
    return render(request, 'accounts/dashboard_directory.html')



# ----------------- ADMIN DASHBOARD -----------------
def admin_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

@admin_required
def admin_dashboard(request):
    pending_vendors = VendorProfile.objects.filter(user__status='pending', user__is_superuser=False)
    all_vendors = VendorProfile.objects.filter(user__is_superuser=False)
    pending_gallery = VendorImage.objects.filter(status='pending')

    return render(request, 'accounts/admin_dashboard.html', {
        'pending_vendors': pending_vendors,
        'all_vendors': all_vendors,
        'pending_gallery': pending_gallery,
    })



# ----------------- VENDOR / GALLERY ACTIONS -----------------
@admin_required
def approve_vendor(request, user_id):
    vendor_user = get_object_or_404(User, id=user_id)
    if vendor_user.status != 'approved':
        vendor_user.status = 'approved'
        vendor_user.save()
        send_email_to_user_and_admin(
            'Account Approved – I Do In Greece',
            f"""Dear {vendor_user.username},

        Your vendor account has been approved.

        You can now log in and upload a profile image in your edit profile page.

        Visit your dashboard here: https://coming soon/dashboard

        Best regards,
        The I Do In Greece Team
        """,
            user_email=vendor_user.email,
            fail_silently=False
        )
        messages.success(request, f"{vendor_user.username} approved successfully.")
    return redirect('admin_dashboard')

@admin_required
def reject_vendor(request, user_id):
    vendor_user = get_object_or_404(User, id=user_id)
    if vendor_user.status != 'rejected':
        vendor_user.status = 'rejected'
        vendor_user.save()
        send_email_to_user_and_admin(
            'Account Rejected – I Do In Greece',
            f"Dear {vendor_user.username},\n\nYour vendor account has been rejected.",
            user_email=vendor_user.email,
            fail_silently=False
        )
        messages.warning(request, f"{vendor_user.username} rejected successfully.")
    return redirect('admin_dashboard')

@admin_required
def delete_vendor(request, user_id):
    vendor_user = get_object_or_404(User, id=user_id)
    vendor_user.delete()
    messages.success(request, "Vendor deleted successfully.")
    return redirect('admin_dashboard')

@admin_required
def approve_gallery(request, image_id):
    image = get_object_or_404(VendorImage, id=image_id)
    image.status = 'approved'
    image.save()
    send_email_to_user_and_admin(
        subject="Gallery Image Approved – I Do In Greece",
        message=(
            f"Hello {image.vendor.user.username},\n\n"
            "We are pleased to inform you that one of your recently uploaded gallery images "
            "has been reviewed and approved by the I Do In Greece admin team.\n\n"
            "Image Details:\n"
            "Your approved images will now be visible to visitors on your profile, "
            "showcasing your work to potential clients.\n\n"
            "Keep uploading high-quality images to enhance your profile and attract more clients.\n\n"
            "Thank you for being a valued vendor on I Do In Greece.\n\n"
            "Best regards,\n"
            "The I Do In Greece Team"
        ),
        user_email=image.vendor.user.email,
        fail_silently=False
    )
    messages.success(request, "Gallery image approved.")
    return redirect('admin_dashboard')

@admin_required
def reject_gallery(request, image_id):
    image = get_object_or_404(VendorImage, id=image_id)
    image.status = 'rejected'
    image.save()
    send_email_to_user_and_admin(
        'Image Rejected – I Do In Greece',
        f"Dear {image.vendor.user.username},\n\nYour gallery image has been reviewed by the admin and was rejected.\n Please kindly reupload a new image to your dashboard.",
        user_email=image.vendor.user.email,
        fail_silently=False
    )
    messages.warning(request, "Gallery image rejected.")
    return redirect('admin_dashboard')

@login_required
def delete_image(request, image_id):
    try:
        image = VendorImage.objects.get(id=image_id)
        if image.vendor.user == request.user:
            image.delete()
            messages.success(request, "Image deleted successfully!")
    except VendorImage.DoesNotExist:
        messages.error(request, "Image not found.")
    return redirect("dashboard")



# ----------------- STRIPE PAYMENT -----------------
@login_required
def stripe_checkout(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'gbp',
                    'product_data': {'name': 'Vendor Subscription'},
                    'unit_amount': 20000,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/payment-success/') + f"?user_id={user.id}",
            cancel_url=request.build_absolute_uri('/payment-cancel/'),
        )
        return redirect(session.url)
    return render(request, 'accounts/stripe_checkout.html', {'user': user})

def payment_success(request):
    user_id = request.GET.get('user_id')
    user = get_object_or_404(User, id=user_id)
    profile = user.vendorprofile

    profile.subscription_type = 'paid'
    profile.subscription_expiry = None
    profile.save()

    user.status = 'approved'
    user.save()

    send_email_to_user_and_admin(
        'Payment Received – Account Approved',
        f"Hi {user.username}, your payment was successful! You can now upload profile & gallery.",
        user_email=user.email,
        fail_silently=False
    )

    messages.success(request, "Payment successful! Your account is approved.")
    return redirect('dashboard')