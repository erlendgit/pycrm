from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.utils.translation import gettext as _

from core.forms import DateConvertForm
from core.lib import next_or_home


def home(request):
    return render(request, 'core/home.html', {
        'title': _('Welcome')
    })


def date_convert(request):
    if request.method == 'POST':
        form = DateConvertForm(data=request.POST)
        if form.is_valid():
            messages.info(request, form.cleaned_data['date_input'])
            return HttpResponseRedirect(next_or_home(request))
    else:
        form = DateConvertForm()

    return render(request, 'core/date_and_time.html', {
        'form': form,
        'title': _("Date convert"),
        'time': timezone.localtime()
    })
