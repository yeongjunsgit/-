from django.urls import path, include
from . import views

urlpatterns = [
    path('lists/', views.lists),
]
