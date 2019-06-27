from django.shortcuts import render, get_object_or_404

from Projects import models


def home(request):
    projects = models.Projects.objects
    return render(request, 'Projects/home.html', {'Projects': projects,
                                                  })


def allprojects(request):
    projects = models.Projects.objects
    return render(request, 'Projects/projects.html', {'Projects': projects})


def projectsdetail(request, project_id):
    projectdetail = get_object_or_404(models.Projects, pk=project_id)
    return render(request, 'Projects/projectsdetails.html', {'projectdetails': projectdetail})
