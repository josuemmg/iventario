from django.urls import path
from . import views
"""""
urlpatterns = [
    path('', views.home, name="home"),
    path('sample/', views.sample, name="sample"),
    path('bienvenido/', views.bienvenido, name="bienvenido"),
    path('desarrollo/', views.desarrollo, name="desarrollo"),
    path('diseño/', views.diseño, name="diseño"),

]
"""""