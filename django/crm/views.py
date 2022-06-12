from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from core.lib import get_object_or_404
from crm.models import Entity


@login_required
def index(request):
    return render(request, 'crm/entity/index.html', {
        "entities": Entity.objects.all()
    })


@login_required
def view(request, id):
    return render(request, 'crm/entity/view.html', {
        'entity': get_object_or_404(Entity, pk=id)
    })


@login_required
def update(request, id):
    return render(request, 'crm/entity/update.html', {
        'entity': get_object_or_404(Entity, pk=id)
    })
