from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from .models import Project, ProjectStudents
from .forms import ProjectForm
from django.utils import timezone

def index(request):
    num_projects = Project.objects.count()
    context = {
        'num_projects': num_projects,
    }
    return render(request, 'index.html', context=context)


def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            students = form.cleaned_data['students']
            for student in students:
                ProjectStudents.objects.create(
                    project=project,
                    student=student,
                    assigned_date=timezone.now()
                )
            return redirect('home')
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'project_detail.html', {'project': project})

def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('home')

def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'edit_project.html', {'form': form, 'project': project})

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'

class ProjectCreateView(CreateView):
    model = Project
    fields = '__all__'
    template_name = 'projects/project_form.html'

class ProjectUpdateView(UpdateView):
    model = Project
    fields = '__all__'
    template_name = 'projects/project_form.html'

class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('projects')
    template_name = 'projects/project_confirm_delete.html'
