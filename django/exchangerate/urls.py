from django.urls import path
from . import views

urlpatterns = [
    path('get_data/', views.get_data),
]
