from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Category

class RecipeViewsTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="For Pineapple")
        self.recipe = Recipe.objects.create(
            title="Recept 2",
            description="Desc for 2",
            instructions="Instruction",
            ingredients="Ingridients for 2",
            category=self.category,
        )

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.recipe.title, 'Recept 2')
        #self.assertContains(response, f"Recipe Name: {self.recipe.title}")

    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipe_detail', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.recipe.title)
