from .models import *
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.forms import  UserCreationForm
from django.views.generic import TemplateView,ListView,DetailView


# Create your views here.
# function based views

# def home(request):
#     return render(request,"myapp/dashboard.html")

# def product(request):
#     product_obj = Product.objects.all()
#     return render(request,"myapp/products.html",{'products':product_obj})

# def customer(request):
#     return render(request,"myapp/customer.html")

# def createOrder(request):
#     return render(request)

class HomeView(TemplateView):
    template_name = "myapp/dashboard.html"

    def get_context_data(self, **kwargs):
        product_obj = Product.objects.all()
        context = {'products':product_obj}
        return context
        
class ProductView(TemplateView):
    template_name = "myapp/products.html"

    def get_context_data(self, **kwargs):
        product_obj = Product.objects.all()
        context = {'products':product_obj}
        return context

class ProductListView(TemplateView):
    template_name = "myapp/products.html"

    def get_queryset(self):
        return Product.objects.all()

class ProductDetailtView(DetailView):
    model = Product
    template_name = "myapp/products_details.html"

    
class CustomerView(TemplateView):
    template_name = "myapp/customer.html"

    def get_context_data(self, **kwargs):
        customer_obj = Customer.objects.all()
        context = {'customer':customer_obj}
        return context


class LoginView(TemplateView):
    template_name = "myapp/login.html"

    # def get_context_data(self, **kwargs):
    #     customer_obj = Customer.objects.all()
    #     context = {'customer':customer_obj}
    #     return context

class RegisterView(TemplateView):

    template_name = "myapp/register.html"
   
    def get_context_data(self, **kwargs):
        form = UserCreationForm()
        context = {'form':form}
        return context

    def post(self,request,**kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        Response({'data':{}}, status=status.HTTP_200_OK)
