from django.urls import path
from . import views
urlpatterns = [
   path('', views.home),
   path('sheettwo/', views.portfolio),
   path('sheetthree/', views.contact),
   path('catalog/', views.application)

]
