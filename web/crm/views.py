from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext as _

from core.lib import get_object_or_404
from crm.forms import EntityUpdateForm, EntityRelationForm, DeleteRelationForm
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
        form = EntityUpdateForm(request.POST, entity=entity)
        if form.is_valid():
            saved = form.update()
            messages.info(request, _("Changes to %(name)s are now stored in the database.") % {"name": saved.name})
            return HttpResponseRedirect(entity.url)
    else:
        form = EntityUpdateForm(entity=entity)

    return render(request, 'crm/page/entity-form.html', {
        'entity': entity,
        'form': form,
        'title': _("Update %(name)s") % {"name": entity.name},
    })


@login_required
def relate(request, id):
    entity = get_object_or_404(Entity, pk=id)
    if request.method == 'POST':
        form = EntityRelationForm(request.POST, entity=entity)
        if form.is_valid():
            relation = form.save()
            messages.info(request, _("%(name)s is now related.") % {"name": relation.reference.name})
            return HttpResponseRedirect(entity.url)
    else:
        form = EntityRelationForm(entity=entity)

    return render(request, 'crm/page/entity-relation-form.html', {
        'entity': entity,
        'form': form,
        'title': _("Add relation to %(name)s") % {"name": entity.name},
    })


@login_required
def delete(request, id):
    entity = get_object_or_404(Entity, pk=id)
    if request.method == 'POST':
        form = DeleteRelationForm(request.POST, entity=entity)
        if form.is_valid():
            form.save()
            messages.info(request, _("Entity %(name)s is removed.") % {"name": entity.name})
            return HttpResponseRedirect(reverse("crm:index"))
    else:
        form = DeleteRelationForm(entity=entity)

    return render(request, 'crm/page/entity-delete-form.html', {
        'entity': entity,
        'form': form,
        'title': _("Delete %(name)s") % {"name": entity.name},
    })


@login_required
def create(request):
    if request.method == 'POST':
        form = EntityUpdateForm(request.POST)
        if form.is_valid():
            entity = form.update()
            messages.info(request, _("Created a new entity."))
            return HttpResponseRedirect(entity.url)
    else:
        form = EntityUpdateForm()

    return render(request, 'crm/page/entity-form.html', {
        'form': form,
        'title': _("Create entity"),
    })
