from django.db.models import Q
from django.urls import reverse
from django.utils.http import urlencode

from webapp.forms import ProjectForm, SimpleSearchForm
from webapp.models import Project
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView


class ProjectView(ListView):
    template_name = 'project/project_view.html'
    model = Project
    context_object_name = 'projects'
    ordering = ['created_at']

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(name__icontains=self.search_value))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_search_form(self):
        return SimpleSearchForm(data=self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

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