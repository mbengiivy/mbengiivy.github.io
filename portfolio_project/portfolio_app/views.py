from django.shortcuts import render, get_object_or_404
from .models import Project, Skill, Experience, Education, About

def index(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    about = About.objects.first() # Get the single About instance

    context = {
        'projects': projects,
        'skills': skills,
        'experiences': experiences,
        'educations': educations,
        'about': about,
    }

    return render(request, 'portfolio_app/index.html', context)

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'portfolio_app/project_detail.html', {'project': project})