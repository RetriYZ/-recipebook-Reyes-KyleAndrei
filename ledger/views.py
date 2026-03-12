from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, RecipeImage, RecipeIngredient
from django.urls import reverse
# Create your views here.

class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipes_list.html'
    context_object_name = 'recipes'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html'
    login_url = '/login/'

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['name']
    template_name = 'ledger/recipe_form.html'


    def form_valid(self, form):
        form.instance.author = self.request.user.profile 
        return super().form_valid(form)

class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    fields = ['image', 'description']
    template_name = 'ledger/add_image.html'

    def form_valid(self, form):
        form.instance.recipe_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.kwargs['pk']})
    
class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = RecipeIngredient 
    fields = ['ingredient', 'quantity']
    template_name = 'ledger/add_ingredient.html'

    def form_valid(self, form):
        form.instance.recipe_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('ledger:recipe_detail', kwargs={'pk': self.kwargs['pk']})