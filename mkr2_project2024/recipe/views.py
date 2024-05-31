from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import date, datetime
from .models import Recipe, Category
from datetime import datetime, timezone


def index(request):
    return HttpResponse("Hello, world. You're at the gallery index.")

def main(request):
    # category = Category.objects.create(
    #         name="For Pineapple",
    #     )
    # category.save()
    # category = Category.objects.all()
    # q = len(category)
    # recipe = Recipe.objects.create(
    #         title="Recept 2",
    #         description="Desc for 2",
    #         instructions="Instruction",
    #         ingredients="Ingridients for 2",
    #         created_at = datetime.now(),
    #         updated_at = datetime.now(),
    #         category_id=2,
    #     )
    # recipe.save()
    recipes = Recipe.objects.all()
    # q = len(recipes)
    return render(
        request,
        'main.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
            'recipes': recipes,
        }
    )

def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(
        request,
        'recipe_detail.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
            'recipe': recipe,
        }
    )