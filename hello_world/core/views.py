from django.shortcuts import render

def index(request):
    context = {
        "glaze_name": "Blue Ash",
        "cone": "Cone 10",
        "color": "Blue / Gray",
        "surface": "Glossy",
        "notes": "This is hard coded. A little test run"
    }

    return render(request, "index.html", context)
