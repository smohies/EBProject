from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('property/<str:value>/', views.properties, name="property")
]