from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    
class Recipe(models.Model):
    name = models.CharField(max_length=100)

class RecipeIngredient(models.Model):
    quantity = models.PositiveIntegerField()
    ingredient = models.ForeignKey(
                                    Ingredient, 
                                    on_delete=models.CASCADE,
                                   related_name='recipe_orders_and_qtys'
                                   )
    recipe = models.ForeignKey(
                                Recipe, 
                                on_delete=models.CASCADE,
                                related__name='ingredients')