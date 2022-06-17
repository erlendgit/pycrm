from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from crm.models import Entity, Reference


class EntityUpdateForm(forms.Form):

    def __init__(self, *args, entity=None, **kwargs):
        super(EntityUpdateForm, self).__init__(*args, **kwargs)
        self.entity = entity
        if self.entity:
            self.initial.update({
                'name': entity.name,
                'pitch': entity.pitch,
            })

    name = forms.CharField(max_length=255, required=True,
                           label=_("Name"))
    pitch = forms.CharField(widget=forms.Textarea(), required=False,
                            label=_("Pitch"))

    def update(self):
        assert self.is_valid(), "There are still errors"
        self.entity.name = self.cleaned_data['name']
        self.entity.pitch = self.cleaned_data['pitch']
        self.entity.save()
        return self.entity

    def create(self):
        assert self.is_valid(), "There are still errors"
        return Entity.objects.create(
            name=self.cleaned_data['name'],
            pitch=self.cleaned_data['pitch'],
        )


class EntityRelationForm(forms.Form):
    reference = forms.ChoiceField(label=_("Relation"))
    relation_type = forms.CharField(label=_("Relation type"))

    def __init__(self, *args, entity, **kwargs):
        super(EntityRelationForm, self).__init__(*args, **kwargs)
        self.entity = entity
        self.fields['reference'].choices = [('', _("Select entity")), *self.get_reference_choices()]

    def get_reference_choices(self):
        return [(o.id, o.name) for o in Entity.objects.exclude(id=self.entity.id)]

    def clean_reference(self):
        try:
            Reference.objects.assert_allowed(self.entity, self.cleaned_data['reference'])
        except AssertionError as e:
            raise ValidationError(e)
        return self.cleaned_data['reference']

    def save(self):
        assert self.is_valid(), "There are still errors"
        return Reference.objects.create(
            entity=self.entity,
            relation_type=self.cleaned_data['relation_type'],
            reference_id=self.cleaned_data['reference'],
        )


class DeleteRelationForm(forms.Form):
    confirm = forms.BooleanField(label=_("I am sure"), required=True)

    def __init__(self, *args, entity, **kwargs):
        super(DeleteRelationForm, self).__init__(*args, **kwargs)
        self.entity = entity

    def save(self):
        assert self.is_valid(), "There are still errors"
        return self.entity.delete()
