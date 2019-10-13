from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from webapp.forms import StatusForm
from webapp.models import Status
from django.views.generic import CreateView, ListView, UpdateView, DeleteView




class StatusView(ListView):
    template_name = 'status/status_view.html'
    model = Status
    context_object_name = 'statuses'


class StatusCreateView(CreateView):
    template_name = 'status/create_status.html'
    model = Status
    fields = ['name']

    def get_success_url(self):
        return reverse('status_view')

class StatusUpdateView(UpdateView):
    model = Status
    template_name = 'status/update_status.html'
    form_class = StatusForm
    context_object_name = 'status'

    def get_success_url(self):
        return reverse('status_view')



class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'status/delete_status.html'
    context_object_name = 'status'
    error = 'error.html'

    def get_success_url(self):
        return reverse('status_view')