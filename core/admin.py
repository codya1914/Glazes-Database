from django.contrib import admin
from .models import Glaze, Ingredient, GlazeIngredient


class GlazeIngredientInline(admin.TabularInline):
    model = GlazeIngredient
    extra = 1


class GlazeAdmin(admin.ModelAdmin):
    list_display = ("name", "cone", "color", "texture", "transparency")
    search_fields = ("name", "color", "texture", "transparency")
    list_filter = ("cone", "color", "texture", "transparency")
    inlines = [GlazeIngredientInline]


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(Glaze, GlazeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(GlazeIngredient)