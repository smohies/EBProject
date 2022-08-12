from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:value>/', views.home, name='page'),
    path('property/<str:value>/', views.properties, name='property'),
    path('contact/', views.contact, name='contact')
]