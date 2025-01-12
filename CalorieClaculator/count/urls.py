from django.urls import path
from . import views

urlpatterns = [
    path ('', views.add_food, name= 'add_food'),
    path('view-food/', views.view_food, name='view_food'),
    path('remove/<int:food_id>/', views.remove_food, name='remove_food'),
    path('reset/', views.reset_calories, name='reset_calories'),
]
