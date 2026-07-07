from django.contrib import admin
from .models import Glaze, Ingredient, GlazeIngredient


class GlazeIngredientInline(admin.TabularInline):
    model = GlazeIngredient
    extra = 1


class GlazeAdmin(admin.ModelAdmin):
    list_display = ("name", "cone", "color", "surface")
    search_fields = ("name", "color", "surface")
    list_filter = ("cone", "color", "surface")
    inlines = [GlazeIngredientInline]


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(Glaze, GlazeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(GlazeIngredient)