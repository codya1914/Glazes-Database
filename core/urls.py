from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_glaze, name="add_glaze"),
    path("glaze/<int:glaze_id>/", views.glaze_detail, name="glaze_detail"),
]