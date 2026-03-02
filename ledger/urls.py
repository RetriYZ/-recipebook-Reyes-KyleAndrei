from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = "ledger"

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipes_list'),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name='recipe_detail'),

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

   
]   