import uuid

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


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

    class Meta:
        ordering = ('name', '-created_at')


class ReferenceManager(models.Manager):
    def assert_allowed(self, entity, reference_id):
        assert str(entity.id) != reference_id, \
            _("References to self are not allowed.")
        assert not self.get_queryset().filter(entity=entity, reference_id=reference_id).exists(), \
            _("Relate only one time from one entity to another.")


class Reference(models.Model):
    created_at = models.DateTimeField(default=timezone.localtime)

    """ What is reference to entity? """
    relation_type = models.CharField(max_length=255)

    entity = models.ForeignKey('crm.Entity', on_delete=models.CASCADE, related_name='references')
    reference = models.ForeignKey('crm.Entity', on_delete=models.CASCADE, related_name='referenced_by')

    objects = ReferenceManager()
