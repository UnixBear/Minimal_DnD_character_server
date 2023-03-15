from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import charSheet
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class CharacterListView(ListView):
    model = charSheet
    template_name = "home.html"

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()  # returns an empty queryset
        return qs


class CharacterDetailView(DetailView):
    model = charSheet
    template_name = "character_details.html"
    context_object_name = "charsheet"


class CharacterCreateView(LoginRequiredMixin, CreateView):
    model = charSheet
    template_name = "character_new.html"
    fields = "__all__"


class CharacterUpdateView(UpdateView):
    model = charSheet
    template_name = "character_update.html"
    fields = "__all__"


class CharacterDeleteView(DeleteView):
    model = charSheet
    template_name = "character_delete.html"
    success_url = reverse_lazy("home")
