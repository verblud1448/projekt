from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
def home(request):
   return render(request, "main/home.html")
def portfolio(request):
   return render(request, "main/portfolio.html")
def contact(request):
   return render(request, "main/contact.html")
def application(request):
   products = Product.objects.all()
   return render(request, 'main/application.html', {'products': products})
