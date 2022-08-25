from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack

# Create your views here.
class SnackListView(ListView):
    template_name: "snack_list.html"
    model = Snack


class SnackDetailView(DetailView):
    template_name: "snack_list.html"
    model = Snack


class SnackCreateView(CreateView):
    template_name: "snack_list.html"
    model = Snack


class SnackUpdateView(UpdateView):
    template_name: "snack_list.html"
    model = Snack


class SnackDeleteView(DeleteView):
    template_name: "snack_list.html"
    model = Snack
