from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeClass.as_view())
]