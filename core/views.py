from .models import Glaze

from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from .forms import GlazeForm
from .models import Ingredient, GlazeIngredient

def index(request):
    glaze_bases = Glaze.objects.all()

    selected_cone = request.GET.get("cone")
    selected_texture = request.GET.get("texture")
    selected_transparency = request.GET.get("transparency")

    print("GET data:", request.GET)
    print("selected_cone:", selected_cone)
    print("selected_texture:", selected_texture)
    print("selected_transparency:", selected_transparency)

    if selected_cone:
        glaze_bases = glaze_bases.filter(cone=selected_cone)

    if selected_texture:
        glaze_bases = glaze_bases.filter(texture=selected_texture)

    if selected_transparency:
        glaze_bases = glaze_bases.filter(transparency=selected_transparency)

    context = {
        "glaze_bases": glaze_bases,
        "selected_cone": selected_cone,
        "selected_texture": selected_texture,
        "selected_transparency": selected_transparency,
    }

    return render(request, "core/index.html", context)


def add_glaze(request):
    if request.method == "POST":
        form = GlazeForm(request.POST)

        if form.is_valid():
            glaze = form.save()

            ingredient_names = request.POST.getlist("ingredient_names")
            ingredient_amounts = request.POST.getlist("ingredient_amounts")

            for name, amount in zip(ingredient_names, ingredient_amounts):
                ingredient, created = Ingredient.objects.get_or_create(name=name)

                GlazeIngredient.objects.create(
                    glaze=glaze,
                    ingredient=ingredient,
                    amount=amount,
                    unit="percent"
                )

            return redirect("index")

    else:
        form = GlazeForm()

    return render(request, "core/add_glaze.html", {"form": form})

def glaze_detail(request, glaze_id):
    glaze = get_object_or_404(Glaze, id=glaze_id)

    ingredients = GlazeIngredient.objects.filter(glaze=glaze)

    total_amount = 0
    for item in ingredients:
        total_amount += item.amount

    context = {
        "glaze": glaze,
        "ingredients": ingredients,
        "total_amount": total_amount,
    }

    return render(request, "core/glaze_detail.html", context)