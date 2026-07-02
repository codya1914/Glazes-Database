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
            "color": "White",
            "cone": "6",
            "texture": "Matte",
            "transparency": "Opaque",
            "description": "A soft matte white base glaze."
        },
        {
            "id": 3,
            "name": "Satin Blue Base",
            "color": "Blue",
            "cone": "7",
            "texture": "Satin",
            "transparency": "Semi-translucent",
            "description": "A satin base that works well with blue colorants."
        },
        {
            "id": 4,
            "name": "Cone 10 Ash Base",
            "color": "Ash",
            "cone": "10",
            "texture": "Glossy",
            "transparency": "Translucent",
            "description": "A high fire ash glaze base."
        },
        {
            "id": 5,
            "name": "Batz’s Opaque with Chrome",
            "cone": "04",
            "texture": "Glossy",
            "transparency": "Opaque",
            "color": "Green",
            "ingredients": [
                {"material": "Frit 3124", "amount": 86.2},
                {"material": "EPK", "amount": 10.35},
                {"material": "Barium Carb", "amount": 3.45},
                {"material": "Bentonite", "amount": 4},
                {"material": "Zircopax", "amount": 10},
            ],
            "additives": [
                {"material": "Chrome", "amount": 0.1, "unit": "%"}
            ],
        },
        {
            "id": 6,
            "name": "Batz’s Opaque with Mason Stain 6456",
            "cone": "04",
            "texture": "Glossy",
            "transparency": "Opaque",
            "color": "Unknown",
            "ingredients": [
                {"material": "Frit 3124", "amount": 86.2},
                {"material": "EPK", "amount": 10.35},
                {"material": "Barium Carb", "amount": 3.45},
                {"material": "Bentonite", "amount": 4},
                {"material": "Zircopax", "amount": 10},
            ],
            "additives": [
                {"material": "Mason Stain 6456", "amount": 3, "unit": "%"}
            ],
        },
    ]

    selected_cone = request.GET.get("cone")
    selected_texture = request.GET.get("texture")
    selected_transparency = request.GET.get("transparency")

    print("GET data:", request.GET)
    print("selected_cone:", selected_cone)
    print("selected_texture:", selected_texture)
    print("selected_transparency:", selected_transparency)

    if selected_cone:
        filtered_glazes = []

        for glaze in glaze_bases:
            if glaze["cone"] == selected_cone:
                filtered_glazes.append(glaze)

        glaze_bases = filtered_glazes


    if selected_texture:
        filtered_glazes = []

        for glaze in glaze_bases:
            if glaze["texture"] == selected_texture:
                filtered_glazes.append(glaze)

        glaze_bases = filtered_glazes


    if selected_transparency:
        filtered_glazes = []

        for glaze in glaze_bases:
            if glaze["transparency"] == selected_transparency:
                filtered_glazes.append(glaze)

        glaze_bases = filtered_glazes

    context = {
        "glaze_bases": glaze_bases
    }
    

    return render(request, "index.html", context)