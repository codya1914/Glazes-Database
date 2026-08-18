from django.urls import path
from . import views

urlpatterns = [
    path(
        "", 
        views.index, 
        name="index"),
    path(
        "add/", 
        views.add_glaze, 
        name="add_glaze"),
    path(
        "glaze/<int:glaze_id>/", 
        views.glaze_detail, 
        name="glaze_detail"),
    path(
        "glaze/<int:glaze_id>/add-photo/",
        views.add_glaze_photo,
        name="add_glaze_photo"),
    path(
        "glaze/<int:glaze_id>/add-variant/", 
        views.add_variant, 
        name="add_variant"),
]