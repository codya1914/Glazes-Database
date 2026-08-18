from django.contrib import admin
from .models import (
    Glaze,
    GlazeIngredient,
    GlazePhoto,
    GlazeVariant,
    VariantAdditive,
    VariantPhoto,
)


class GlazeIngredientInline(admin.TabularInline):
    model = GlazeIngredient
    extra = 1


class GlazePhotoInline(admin.TabularInline):
    model = GlazePhoto
    extra = 1


class VariantAdditiveInline(admin.TabularInline):
    model = VariantAdditive
    extra = 1


class VariantPhotoInline(admin.TabularInline):
    model = VariantPhoto
    extra = 1


@admin.register(Glaze)
class GlazeAdmin(admin.ModelAdmin):
    list_display = ("name", "cone", "texture", "transparency")
    inlines = [GlazeIngredientInline, GlazePhotoInline]


@admin.register(GlazeVariant)
class GlazeVariantAdmin(admin.ModelAdmin):
    list_display = ("name", "glaze", "color")
    inlines = [VariantAdditiveInline, VariantPhotoInline]


admin.site.register(VariantAdditive)
admin.site.register(VariantPhoto)