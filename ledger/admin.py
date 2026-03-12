from django.contrib import admin
from .models import RecipeIngredient, Recipe, Ingredient, Profile, RecipeImage
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInLine]
    list_display = ('name', 'author', 'created_on', 'updated_on')

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1 

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    inlines = [RecipeImageInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Profile)
