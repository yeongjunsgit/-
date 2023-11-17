from django.urls import path, include
from . import views

urlpatterns = [
    path('lists/', views.lists),
    path('manage/<int:article_pk>/', views.manage_article),
]
