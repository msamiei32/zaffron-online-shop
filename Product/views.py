from django.shortcuts import render
from django.views.generic import DetailView,ListView
from .models import Product
# Create your views here.


class ProductView(ListView):
    model = Product
    context_object_name = 'product'
    template_name = 'registration/productListview.html'