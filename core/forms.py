from django import forms
from .models import Glaze, GlazePhoto, GlazeVariant, VariantAdditive, VariantPhoto


class GlazeForm(forms.ModelForm):
    class Meta:
        model = Glaze
        fields = [
            "name",
            "cone",
            "texture",
            "transparency",
            "notes",
        ]


class GlazePhotoForm(forms.ModelForm):
    class Meta:
        model = GlazePhoto
        fields = [
            "image",
            "caption",
        ]


class GlazeVariantForm(forms.ModelForm):
    class Meta:
        model = GlazeVariant
        fields = [
            "name",
            "color",
            "notes",
        ]


class VariantAdditiveForm(forms.ModelForm):
    class Meta:
        model = VariantAdditive
        fields = [
            "name",
            "amount",
        ]


class VariantPhotoForm(forms.ModelForm):
    class Meta:
        model = VariantPhoto
        fields = [
            "image",
            "caption",
        ]