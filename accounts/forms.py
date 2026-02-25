from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, VendorProfile


class VendorSignupForm(UserCreationForm):
    business_name = forms.CharField(max_length=255)
    bio = forms.CharField(widget=forms.Textarea)
    location = forms.CharField(max_length=255)

    class Meta:
        model = User
        # Explicit order: username, email, password1, password2, then vendor fields
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "business_name",
            "bio",
            "location",
        ]

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
            )
        return user