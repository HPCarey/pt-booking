from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='home'),
    path('add_booking/', views.add_booking, name='add_booking'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path(
        'update_booking/<int:id>', views.update_booking, name='update_booking'
        ),
    path(
        'delete_booking/<int:id>', views.delete_booking, name='delete_booking'
        ),


]
