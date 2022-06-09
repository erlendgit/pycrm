from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm, UserChangeForm as BaseUserChangeForm

from user.models import User


class UserCreationForm(BaseUserCreationForm):

    class Meta:
        model = User
        fields = ('email',)


class UserChangeForm(BaseUserChangeForm):

    class Meta:
        model = User
        fields = ('email',)