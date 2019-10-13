from django.urls import reverse
from webapp.forms import TrackerForm
from webapp.models import Tracker
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView




class IndexView(ListView):
    template_name = 'tracker/index.html'
    model = Tracker
    context_object_name = 'trackers'
    ordering = ['-created_at']
    paginate_by = 2
    paginate_orphans = 1




class TrackerView(DetailView):
    template_name = 'tracker/detailed.html'
    model = Tracker
    context_key = 'tracker'



class TrackerCreateView(CreateView):
    template_name = 'tracker/create.html'
    model = Tracker
    form_class = TrackerForm
    # fields = ['summary', 'description', 'status', 'type']

    def get_success_url(self):
        return reverse('tracker_view', kwargs={'pk': self.object.pk})




class TrackerUpdateView(UpdateView):
    model = Tracker
    template_name = 'tracker/update.html'
    form_class = TrackerForm
    context_object_name = 'issue'
    def get_success_url(self):
        return reverse('tracker_view', kwargs={'pk': self.object.pk})


class TrackerDeleteView(DeleteView):
    model = Tracker
    template_name = 'tracker/delete.html'
    context_object_name = 'issue'


    def get_success_url(self):
        return reverse('index')