from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import charSheet
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import models
from django.views.generic.edit import FormView
from .forms import CharacterForm

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


class CharacterDetailTestingView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = charSheet
    template_name = "character_details_testing.html"
    context_object_name = "charsheet"
    stats_for_bonus = ["charStr", "charDex", "charCon", "charInt", "charWis", "charCha"]
    fields = [
        field.name for field in charSheet._meta.get_fields() if field.name != "author"
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["character"] = self.object
        context["form"] = CharacterForm()

        modified_fields = self.object.get_stat_bonuses(self.stats_for_bonus)
        context.update(modified_fields)

        return context

    def get_success_url(self):
        return reverse_lazy(
            "characters:character_details_testing", kwargs={"pk": self.object.pk}
        )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"instance": self.object})
        return kwargs

    def get_object(self):
        return get_object_or_404(charSheet, pk=self.kwargs["pk"])

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Character details saved successfully.")
        print("testing")
        return response

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class CharacterCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = charSheet
    template_name = "character_new.html"
    fields = [
        field.name for field in charSheet._meta.get_fields() if field.name != "author"
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class CharacterUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = charSheet
    template_name = "character_update.html"
    fields = [
        field.name for field in charSheet._meta.get_fields() if field.name != "author"
    ]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class CharacterDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = charSheet
    template_name = "character_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
