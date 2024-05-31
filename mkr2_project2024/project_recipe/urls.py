from django.contrib import admin
from django.urls import path, include
from recipe import views


urlpatterns = [
    path('', views.main, name='main'),
    path('recipe_detail/<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('admin/', admin.site.urls),
]