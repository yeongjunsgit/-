from django.urls import path, include
from . import views

urlpatterns = [
    # path('signup/', views.signup),
    path('user-detail/',views.user_detail),
    path('add-data/',views.add_data)
]   