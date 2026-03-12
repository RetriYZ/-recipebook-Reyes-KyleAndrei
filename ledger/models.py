from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=255)

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:ingredient_detail', args=[str(self.name)])
    
class Recipe(models.Model):
    name = models.CharField(max_length=100)

    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='recipes', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)   
    updated_on = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[self.pk])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE,
        related_name='recipe_placements_and_qtys'
        )
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE,
        related_name='ingredients'
        )
    
    def __str__(self): 
        return f"{self.quantity} of {self.ingredient.name} for {self.recipe.name}"
    
class RecipeImage(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='recipe_images/')
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"Image for {self.recipe.name}"