from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='home'),
    path('add_booking/', views.add_booking, name='add_booking'),
    path('user_profile/', views.user_profile, name='user_profile'),
]
