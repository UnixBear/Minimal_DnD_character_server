from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import charSheet

# Create your views here.


class CharacterListView(ListView):
    model = charSheet
    template_name = "home.html"


class CharacterDetailView(DetailView):
    model = charSheet
    template_name = "character_details.html"
    context_object_name = "charsheet"

    
