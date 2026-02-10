from django.urls import path
from . import views

app_name = "ledger"
urlpatterns = [
    path('', views.recipes_list, name='recipes_list'),
    path('', views.recipe1, name='recipe1'),
    path('', views.recipe2, name='recipe2'),
]