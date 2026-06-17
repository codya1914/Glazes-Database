from django.shortcuts import render

def index(request):
    glaze_bases = [
        {
            "id": 1,
            "name": "Clear Gloss Base",
            "cone": "6",
            "texture": "Glossy",
            "transparency": "Translucent",
            "description": "A clear glossy base glaze used for color testing."
        },
        {
            "id": 2,
            "name": "Matte White Base",
            "cone": "6",
            "texture": "Matte",
            "transparency": "Opaque",
            "description": "A soft matte white base glaze."
        },
        {
            "id": 3,
            "name": "Satin Blue Base",
            "cone": "7",
            "texture": "Satin",
            "transparency": "Semi-translucent",
            "description": "A satin base that works well with blue colorants."
        },
        {
            "id": 4,
            "name": "Cone 10 Ash Base",
            "cone": "10",
            "texture": "Glossy",
            "transparency": "Translucent",
            "description": "A high fire ash glaze base."
        },
    ]

    selected_cone = request.GET.get("cone")
    selected_texture = request.GET.get("texture")
    selected_transparency = request.GET.get("transparency")

    if selected_cone:
        glaze_bases = [glaze for glaze in glaze_bases if glaze["cone"] == selected_cone]

    if selected_texture:
        glaze_bases = [glaze for glaze in glaze_bases if glaze["texture"] == selected_texture]

    if selected_transparency:
        glaze_bases = [glaze for glaze in glaze_bases if glaze["transparency"] == selected_transparency]

    context = {
        "glaze_bases": glaze_bases,
    }

    return render(request, "index.html", context)