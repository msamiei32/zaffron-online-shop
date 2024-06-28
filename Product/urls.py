from django.urls import path
from .views import ProductView

app_name = 'Product'
urlpatterns = [
    path('productlist/',ProductView.as_view(),name = 'productlist')
]