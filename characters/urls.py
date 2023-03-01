from django.urls import path
from .views import CharacterListView, CharacterDetailView

urlpatterns = [
    path("", CharacterListView.as_view(), name="home"),
    path(
        "<str:author>/character/<int:pk>/",
        CharacterDetailView.as_view(),
        name="character_details",
    ),
]
