from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from App_Login.models import UserProfile
from django.urls import reverse


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email Address", required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].help_text = (
            "Raw passwords are not stored, so there is no way to see this "
            "user’s password, but you can change the password using "
            '<a href="{}">this form</a>.'
        ).format(reverse("App_Login:password_change"))


class ProfilePic(forms.ModelForm):
    class Meta:
        model = UserProfile
        # fields = ('profile_pic',)
        fields = ['profile_pic',]
        labels = {'profile_pic':'Profile Picture',}
        widgets = {
            'profile_pic': forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),
        }
        



