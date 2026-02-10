from django.urls import path
from . import views

app_name = "ledger"
urlpatterns = [
    path('', views.recipes_list, name='recipes_list'),
    path('recipe/1', views.recipe1, name='recipe1'),
    path('recipe/2', views.recipe2, name='recipe2'),
]