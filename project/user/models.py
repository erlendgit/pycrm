import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email must be set...")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser should have is_staff=True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser should have is_superuser=True")
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    objects = UserManager()

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    email = models.EmailField(_("email address"), unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("User account")
        verbose_name_plural = _("User accounts")