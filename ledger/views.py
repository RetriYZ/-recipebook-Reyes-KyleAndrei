from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Recipe
# Create your views here.

def recipes_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'ledger/recipes_list.html', {'recipes': recipes})

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    return render(request, 'ledger/recipe_detail.html', {'recipe': recipe})