from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, VendorProfile


class VendorSignupForm(UserCreationForm):
    business_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your business name"
        })
    )

    bio = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Tell customers about your business...",
            "rows": 4
        })
    )

    location = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your business location"
        })
    )

    # ✅ NEW FIELDS
    age = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your age"
        })
    )

    gender = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your gender"
        })
    )

    phone_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your phone number"
        })
    )

    county_of_residence = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your county of residence"
        })
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Choose a username"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your email"
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

        self.fields["business_name"].label = "Business Name"
        self.fields["bio"].label = "Business Description"
        self.fields["location"].label = "Business Location"

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_vendor = True

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
            "age",
            "gender",
            "phone_number",
            "county_of_residence",
            "profile_image"
        ]

        widgets = {
            "business_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Update business name"
            }),
            "bio": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Update business description"
            }),
            "location": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Update location"
            }),
            "age": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Update age"
            }),
            "gender": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Update gender"
            }),
            "phone_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Update phone number"
            }),
            "county_of_residence": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Update county of residence"
            }),
            "profile_image": forms.FileInput(attrs={
                "class": "form-control"
            }),
        }