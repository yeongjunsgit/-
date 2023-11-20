from django.urls import path, include
from . import views

urlpatterns = [
    # path('signup/', views.signup),
    path('user_detail/',views.user_detail)
]   