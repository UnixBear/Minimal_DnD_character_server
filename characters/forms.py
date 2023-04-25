from django import forms
from .models import charSheet


class CharacterForm(forms.ModelForm):
    class Meta:
        model = charSheet
        fields = [
            field.name
            for field in charSheet._meta.get_fields()
            if field.name != "author"
        ]
        # fields = "__all__"
