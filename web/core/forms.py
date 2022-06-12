from django import forms
from django.utils.translation import gettext as _


class DateConvertForm(forms.Form):
    date_input = forms.DateTimeField(label=_("Date and time"))