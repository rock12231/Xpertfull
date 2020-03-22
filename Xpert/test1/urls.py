from django.urls import path
from test1 import views

urlpatterns = [

    path('webtest/', views.owner, name="owner"),
]