from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext as _

from core.lib import get_object_or_404
from crm.forms import EntityUpdateForm
from crm.models import Entity


@login_required
def index(request):
    return render(request, 'crm/page/entity-index.html', {
        "entities": Entity.objects.all(),
        "title": _("Entities"),
    })


@login_required
def view(request, id):
    entity = get_object_or_404(Entity, pk=id)
    return render(request, 'crm/page/entity-view.html', {
        'entity': entity,
        "title": entity.name
    })


@login_required
def update(request, id):
    entity = get_object_or_404(Entity, pk=id)
    if request.method == 'POST':
        form = EntityUpdateForm(request.POST)
        if form.is_valid():
            entity.name = form.cleaned_data['name']
            entity.pitch = form.cleaned_data['pitch']
            entity.save()
            return HttpResponseRedirect(reverse("crm:view", args=[entity.id]))
    else:
        form = EntityUpdateForm(entity=entity)

    return render(request, 'crm/page/entity-update.html', {
        'entity': entity,
        'form': form,
        'title': _("Update %(name)s") % {"name": entity.name},
    })
