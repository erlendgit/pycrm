import logging

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm, UserChangeForm as BaseUserChangeForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from user.models import User

logger = logging.getLogger(__name__)


class UserCreationForm(BaseUserCreationForm):

    class Meta:
        model = User
        fields = ('email',)


class UserChangeForm(BaseUserChangeForm):

    class Meta:
        model = User
        fields = ('email',)


class UserLoginForm(forms.Form):
    user = None
    email = forms.CharField(label=_("E-mail"), required=True)
    password = forms.CharField(label=_("Password"), required=True,
                               widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}))
    next = forms.CharField(widget=forms.HiddenInput())

    def clean_password(self):
        self.user = authenticate(username=self.cleaned_data['email'],
                                 password=self.cleaned_data['password'])
        if not self.user:
            raise ValidationError(_("Username or password is incorrect."))

        return self.cleaned_data['password']