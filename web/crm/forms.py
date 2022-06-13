from django import forms
from django.utils.translation import gettext_lazy as _


class EntityUpdateForm(forms.Form):
    def __init__(self, *args, entity=None, **kwargs):
        super(EntityUpdateForm, self).__init__(*args, **kwargs)
        if entity:
            self.initial.update({
                'name': entity.name,
                'pitch': entity.pitch,
            })

    name = forms.CharField(max_length=255, required=True,
                           label=_("Name"))
    pitch = forms.CharField(widget=forms.Textarea(), required=False,
                            label=_("Pitch"))
