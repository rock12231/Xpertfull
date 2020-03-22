from django.urls import path
from images import views

urlpatterns = [

    path('images/', views.image, name="image"),
    path('owner/', views.owner_data, name="owner_data"),
    path('owner/', views.owner, name="owner"),
    path('', views.index, name="index"),
    path('delete/<str:pk>/', views.delete, name="delete"),
]