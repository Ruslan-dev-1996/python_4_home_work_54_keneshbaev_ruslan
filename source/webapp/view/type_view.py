from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from webapp.forms import TypeForm
from webapp.models import Type
from django.views.generic import CreateView,  ListView, UpdateView, DeleteView




class TypeView(ListView):
    template_name = 'type/type_view.html'
    model = Type
    context_key = 'types'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_key] = self.model.objects.all()
        return context

class TypeCreateView(CreateView):
    template_name = 'type/create_type.html'
    model = Type
    fields = ['type']

    def get_success_url(self):
        return reverse('type_view')



class TypeUpdateView(UpdateView):
    model = Type
    template_name = 'type/update_type.html'
    form_class = TypeForm
    context_object_name = 'type'

    def get_success_url(self):
        return reverse('type_view')



class TypeDeleteView(DeleteView):
    model = Type
    template_name = 'type/delete_type.html'
    context_object_name = 'type'
    error = 'error_type.html'

    def get_success_url(self):
        return reverse('type_view' )