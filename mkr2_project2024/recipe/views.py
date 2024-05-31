from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from .models import Recipe, Category
from datetime import datetime, timezone


def index(request):
    return HttpResponse("Hello, world. You're at the gallery index.")

def main(request):
    category = Category.objects.create(
            name="For Pineapple",
        )
    category.save()
    category = Category.objects.all()
    q = len(category)
    # recipe = Recipe.objects.create(
    #         title="Recept 1",
    #         description="Desc for 1",
    #         instructions="Instruction",
    #         ingredients="Ingridients for 1",
    #         created_at = timezone.now(),
    #         updated_at = timezone.now(),
    #         category_id=1,
    #     )
    # recipe.save()

    return render(
        request,
        'main.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )

def recipe_detail(request):
    return render(
        request,
        'recipe_detail.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )