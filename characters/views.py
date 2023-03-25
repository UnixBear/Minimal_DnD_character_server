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
from django.db import models

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


class CharacterDetailTestingView(DetailView):
    model = charSheet
    template_name = "character_details_testing.html"
    context_object_name = "charsheet"
    stats_for_bonus = ["charStr", "charDex", "charCon", "charInt", "charWis", "charCha"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        modified_fields = self.object.get_stat_bonuses(self.stats_for_bonus)
        context.update(modified_fields)

        return context


class CharacterCreateView(LoginRequiredMixin, CreateView):
    model = charSheet
    template_name = "character_new.html"
    fields = [
        field.name for field in charSheet._meta.get_fields() if field.name != "author"
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CharacterUpdateView(UpdateView):
    model = charSheet
    template_name = "character_update.html"
    fields = [
        field.name for field in charSheet._meta.get_fields() if field.name != "author"
    ]


class CharacterDeleteView(DeleteView):
    model = charSheet
    template_name = "character_delete.html"
    success_url = reverse_lazy("home")
