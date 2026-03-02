from django.contrib import admin
from .models import RecipeIngredient, Recipe, Ingredient
# Register your models here.

class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInLine]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
