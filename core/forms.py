from .models import Glaze
from django import forms

class GlazeForm(forms.ModelForm):
    class Meta:
        model = Glaze
        fields = ["name", "cone", "color", "texture", "transparency", "notes", "image"]