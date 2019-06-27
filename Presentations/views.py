from django.shortcuts import render, get_object_or_404

from Presentations import models


def allpresentations(request):
    presentations = models.Presentations.objects
    return render(request, 'Presentations/presentations.html', {'presentation': presentations})


def presentationsdetail(request, presentation_id):
    detailpresentation = get_object_or_404(models.Presentations, pk=presentation_id)
    return render(request, 'Presentations/presentationsdetail.html', {'presentations': detailpresentation})