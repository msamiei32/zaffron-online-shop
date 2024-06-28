from django.contrib import admin
from .models import Specifications,Brand,Category,Product
# Register your models here.


admin.site.register(Specifications)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)