from django.urls import path
from .views import (
    CharacterListView,
    CharacterDetailView,
    CharacterCreateView,
    CharacterUpdateView,
    CharacterDeleteView,
    CharacterDetailTestingView,
)

urlpatterns = [
    path("", CharacterListView.as_view(), name="home"),
    path(
        "<str:author>/character/<int:pk>/",
        CharacterDetailView.as_view(),
        name="character_details",
    ),
    path(
        "character/new/",
        CharacterCreateView.as_view(),
        name="character_new",
    ),
    path(
        "<str:author>/character/<int:pk>/edit",
        CharacterUpdateView.as_view(),
        name="character_update",
    ),
    path(
        "<str:author>/character/<int:pk>/delete",
        CharacterDeleteView.as_view(),
        name="character_delete",
    ),
    path(
        "<str:author>/character/<int:pk>/testing",
        CharacterDetailTestingView.as_view(),
        name="character_details_testing",
    ),
]
