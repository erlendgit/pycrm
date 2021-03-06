import logging

from django.contrib.auth import login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.urls import reverse

from core.lib import next_or_home
from user.forms import UserLoginForm

logger = logging.getLogger(__name__)


def default(request):
    return HttpResponsePermanentRedirect(reverse('user:login'))


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            django_login(request, form.user)
            return HttpResponseRedirect(next_or_home(request))
    else:
        form = UserLoginForm(initial={"next": next_or_home(request)})

    return render(request, 'user/login.html', {
        "form": form,
    })


@login_required
def logout(request):
    django_logout(request)
    return HttpResponseRedirect(next_or_home(request))
