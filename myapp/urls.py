from django.urls import path,include
from .views import *

urlpatterns = [
    path('home/',HomeView.as_view(),name='home'),
    path('products/',ProductView.as_view(),name='products'),
    path('products-list/',ProductListView.as_view(),name='products-list'),
    path('products-details/<int:pk>',ProductDetailtView.as_view(),name='products-details'),
    path('customer/',CustomerView.as_view(),name='customer'),
    path('login/',LoginView.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
]
