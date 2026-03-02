from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe
# Create your views here.

class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipes_list.html'
    context_object_name = 'recipes'

class RecipeDetailView(LoginRequiredMixin, DetailView):
        model = Recipe
        template_name = 'ledger/recipe_detail.html'
        login_url = '/login/'