from django.shortcuts import render, redirect, get_object_or_404
from .models import Glaze, GlazeIngredient, VariantAdditive, GlazePhoto, VariantPhoto, GlazeVariant
from .forms import GlazeForm, GlazeVariantForm, GlazePhotoForm

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

            # -------------------------
            # SAVE INGREDIENTS
            # -------------------------

            ingredient_names = request.POST.getlist("ingredient_name")
            ingredient_amounts = request.POST.getlist("ingredient_amount")

            for name, amount in zip(ingredient_names, ingredient_amounts):
                if name.strip() or amount.strip():
                    GlazeIngredient.objects.create(
                        glaze=glaze,
                        name=name,
                        amount=amount
                    )

            # -------------------------
            # SAVE IMAGES
            # -------------------------

            images = request.FILES.getlist("images")

            for image in images:
                GlazePhoto.objects.create(
                    glaze=glaze,
                    image=image
                )

            return redirect(
                "glaze_detail",
                glaze_id=glaze.id
            )

    else:
        form = GlazeForm()

    return render(
        request,
        "core/add_glaze.html",
        {
            "form": form,
        }
    )

def glaze_detail(request, glaze_id):
    glaze = get_object_or_404(Glaze, id=glaze_id)

    ingredients = glaze.ingredients.all()

    return render(request, "core/glaze_detail.html", {
        "glaze": glaze,
        "ingredients": ingredients,
    })

def add_glaze_photo(request, glaze_id):
    glaze = get_object_or_404(Glaze, id=glaze_id)

    if request.method == "POST":
        form = GlazePhotoForm(request.POST, request.FILES)

        if form.is_valid():
            photo = form.save(commit=False)
            photo.glaze = glaze
            photo.save()

    return redirect("glaze_detail", glaze_id=glaze.id)

def delete_glaze_photo(request, glaze_id, photo_id):
    glaze = get_object_or_404(Glaze, id=glaze_id)
    photo = get_object_or_404(
        GlazePhoto,
        id=photo_id,
        glaze=glaze
    )

    if request.method == "POST":
        photo.delete()

    return redirect("glaze_detail", glaze_id=glaze.id)

def add_variant(request, glaze_id):
    glaze = get_object_or_404(Glaze, id=glaze_id)

    if request.method == "POST":
        form = GlazeVariantForm(request.POST)

        if form.is_valid():
            variant = form.save(commit=False)
            variant.glaze = glaze
            variant.save()

            # -------------------------
            # SAVE ADDITIVES
            # -------------------------

            additive_names = request.POST.getlist("additive_name")
            additive_amounts = request.POST.getlist("additive_amount")

            for name, amount in zip(
                additive_names,
                additive_amounts
            ):
                if name.strip() or amount.strip():
                    VariantAdditive.objects.create(
                        variant=variant,
                        name=name,
                        amount=amount
                    )

            # -------------------------
            # SAVE IMAGES
            # -------------------------

            images = request.FILES.getlist("images")

            for image in images:
                VariantPhoto.objects.create(
                    variant=variant,
                    image=image
                )

            return redirect(
                "glaze_detail",
                glaze_id=glaze.id
            )

    else:
        form = GlazeVariantForm()

    return render(
        request,
        "core/add_variant.html",
        {
            "form": form,
            "glaze": glaze,
        }
    )

def delete_variant(request, glaze_id, variant_id):
    glaze = get_object_or_404(Glaze, id=glaze_id)

    variant = get_object_or_404(
        GlazeVariant,
        id=variant_id,
        glaze=glaze
    )

    if request.method == "POST":
        variant.delete()

    return redirect("glaze_detail", glaze_id=glaze.id)