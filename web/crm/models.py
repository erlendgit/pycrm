import uuid

from django.db import models
from django.urls import reverse


class EntityManager(models.Manager):
    pass


class Entity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    pitch = models.TextField(null=True, blank=True, default=None)
    profile = models.JSONField(null=True, blank=True, default=None)

    objects = EntityManager()

