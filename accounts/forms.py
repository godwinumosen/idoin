from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, VendorProfile


class VendorSignupForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your first name"
        })
    )

    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your last name"
        })
    )

    # ✅ Terms & Conditions checkbox
    terms = forms.BooleanField(
        required=True,
        label='I have read and agree to the Terms and Conditions',
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
            "terms",  # added
        ]
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Choose a username"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your valid email"
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Create password"
        })
        self.fields["password2"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Confirm password"
        })
        self.fields["first_name"].label = "First Name"
        self.fields["last_name"].label = "Last Name"
    

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_vendor = True

        # ✅ Save first_name and last_name
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        if commit:
            user.save()
            VendorProfile.objects.create(
                user=user,
                business_name=self.cleaned_data["business_name"],
                bio=self.cleaned_data["bio"],
                location=self.cleaned_data["location"],
                age=self.cleaned_data["age"],
                gender=self.cleaned_data["gender"],
                phone_number=self.cleaned_data["phone_number"],
                county_of_residence=self.cleaned_data["county_of_residence"],
            )

        return user


class VendorProfileForm(forms.ModelForm):
    class Meta:
        model = VendorProfile
        fields = [
            "business_name",
            "bio",
            "location",
            "category",
            "phone_number",
            "profile_image",
            "instagram",
            "facebook",
            "tiktok",
        ]
        labels = {
            "business_name": "Business Name",
            "bio": "Business Description",
            "location": "Business Location",
            "category": "Category",
            "phone_number": "Phone Number",
            "profile_image": "Profile Image"
        }
        widgets = {
            "business_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Update Business name"
            }),
            "bio": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Update Business description"
            }),
            "location": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Update location"
            }),

            "category": forms.Select(attrs={
                "class": "form-control"
            
            }),
  
            "phone_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Update phone number"
            }),
  
            "profile_image": forms.FileInput(attrs={
                "class": "form-control"
            }),
            "instagram": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "Instagram profile link"
            }),
            "facebook": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "Facebook page link"
            }),
            "tiktok": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "TikTok profile link"
            }),
        }