from django.urls import reverse
from django.utils.http import urlencode
from django.db.models import Q
from webapp.forms import TrackerForm, SimpleSearchForm
from webapp.models import Tracker
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView




class IndexView(ListView):
    template_name = 'tracker/index.html'
    model = Tracker
    context_object_name = 'trackers'
    ordering = ['-created_at']
    paginate_by = 2
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value))
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