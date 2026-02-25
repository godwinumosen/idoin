from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import VendorProfileForm, VendorSignupForm
from .models import VendorProfile, VendorImage
from django.core.mail import send_mail

# Signup view
def signup_view(request):
    if request.method == "POST":
        form = VendorSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.status = 'pending'  # default
            user.save()
            form.save_m2m()  # if needed

            # Send email to user confirming registration
            send_mail(
                subject='Registration Received',
                message=(
                    f"Dear {user.username},\n\n"
                    "Thank you for registering with I Do In Greece. "
                    "We are delighted to receive your application to join our trusted vendor directory.\n\n"
                    "Your account has been successfully created and is currently pending review by our administrative team. "
                    "This approval process allows us to maintain the highest standards of quality, reliability, and professionalism "
                    "across our platform.\n\n"
                    "Once your account has been reviewed and approved, you will receive a confirmation email with further instructions. "
                    "If any additional information is required during the review process, our team will contact you directly.\n\n"
                    "We truly appreciate your interest in partnering with I Do In Greece and look forward to potentially showcasing "
                    "your services to couples planning their special day.\n\n"
                    "Warm regards,\n"
                    "The I Do In Greece Team"
                ),
                from_email='no-reply@yourdomain.com',
                recipient_list=[user.email],
                fail_silently=False,
            )
            return redirect('login')
    else:
        form = VendorSignupForm()
    return render(request, "accounts/signup.html", {"form": form})




# views.py or a custom authentication backend
from django.contrib.auth import authenticate, login
from django.contrib import messages

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
            else:  # rejected
                messages.error(request, "Your account has been rejected")
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, 'accounts/login.html')



@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def edit_profile(request):
    profile = request.user.vendorprofile

    if request.method == "POST":
        form = VendorProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = VendorProfileForm(instance=profile)

    return render(request, "accounts/edit_profile.html", {"form": form})






@login_required
def delete_image(request, image_id):
    image = VendorImage.objects.get(id=image_id)
    if image.vendor.user == request.user:
        image.delete()
    return redirect("dashboard")



# Upload image (AJAX)
@login_required
def upload_gallery_image(request):
    profile = request.user.vendorprofile

    if request.user.status != "approved":
        return JsonResponse({"error": "Account not approved"}, status=403)

    if profile.gallery.count() >= 10:
        return JsonResponse({"error": "Gallery full"}, status=400)

    if request.method == "POST":
        image = request.FILES.get("image")
        if image:
            VendorImage.objects.create(vendor=profile, image=image)
            return JsonResponse({"success": True})

    return JsonResponse({"error": "No image uploaded"}, status=400)




@login_required
def dashboard(request):
    profile = None
    gallery = None

    # Check if user is vendor
    if request.user.is_vendor:
        try:
            profile = request.user.vendorprofile
            gallery = profile.gallery.all()
        except VendorProfile.DoesNotExist:
            profile = None
            gallery = None

    # Collect general user info
    user_info = {
        "username": request.user.username,
        "email": request.user.email,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "date_joined": request.user.date_joined,
        "is_vendor": request.user.is_vendor,
        "status": request.user.get_status_display() if request.user.is_vendor else None,
    }

    return render(
        request,
        "accounts/dashboard.html",
        {
            "profile": profile,
            "gallery": gallery,
            "user_info": user_info
        }
    )



