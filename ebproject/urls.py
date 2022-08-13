from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:value>/', views.home, name='page'),
    path('property/<str:property_id>/', views.properties, name='property'),
    path('lead/', views.leads, name='lead')
]