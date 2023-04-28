from django.shortcuts import render

# список рецептов
DATA = {
    "omlet": {
        "eggs": 2,
        "milk": 0.1,
        "salt": 0.5,
    },
    "pasta": {
        "pasta": 0.2,
        "cheese": 0.03,
        "milk": 0.02,
        "butter": 0.01,
    },
}

# функции для обработки запросов
def omlet(request):
    servings = int(request.GET.get("servings", 1))
    context = {"recipe": {}}
    for ingredient, amount in DATA["omlet"].items():
        context["recipe"][ingredient] = amount * servings
    return render(request, "recipe.html", context)

def pasta(request):
    servings = int(request.GET.get("servings", 1))
    context = {"recipe": {}}
    for ingredient, amount in DATA["pasta"].items():
        context["recipe"][ingredient] = amount * servings
    return render(request, "recipe.html", context)