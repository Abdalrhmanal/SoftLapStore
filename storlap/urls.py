from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.BASE , name='BASE'),
    path('category', views.Category , name='Category'),
    path('detailsproduct', views.DetailsProduct , name='DetailsProduct'),
    path('cart', views.Cart , name='Cart'),
    path('contact', views.Contact , name='Contact'),
    path('login', views.Login , name='Login'),
    path('register', views.Register , name='Register'),
]
