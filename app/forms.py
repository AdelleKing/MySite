"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import PasswordChangeForm

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))



class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    phone = forms.RegexField(regex=r'^\d{11}$')
    email = forms.EmailField(required=True)
    content = forms.CharField(widget=forms.Textarea, required = True)


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].widget.attrs.update({"class": "form-control", "placeholder": "Enter current password"})
        self.fields["new_password1"].widget.attrs.update({"class": "form-control", "placeholder": "Enter new password"})
        self.fields["new_password2"].widget.attrs.update({"class": "form-control", "placeholder": "Confirm new password"})