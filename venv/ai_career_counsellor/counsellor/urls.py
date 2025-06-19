from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.user_profile_form, name='user_form'),
    path('suggestions/<int:user_id>/', views.career_suggestions, name='career_suggestions'),
]
