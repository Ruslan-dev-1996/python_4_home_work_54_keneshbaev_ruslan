from django.urls import reverse
from webapp.forms import ProjectForm
from webapp.models import Project
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView


class ProjectView(ListView):
    template_name = 'project/project_view.html'
    model = Project
    context_object_name = 'projects'
    ordering = ['created_at']


class ProjectDetailView(DetailView):
    template_name = 'project/detail_project.html'
    model = Project
    context_object_name = 'project'


class ProjectCreateView(CreateView):
    template_name = 'project/create_project.html'
    model = Project
    form_class = ProjectForm
    def get_success_url(self):
        return reverse('project_view')

class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project/update_project.html'
    form_class = ProjectForm
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project_view')



class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project/delete_project.html'
    context_object_name = 'project'
    # error = 'error.html'

    def get_success_url(self):
        return reverse('project_view')