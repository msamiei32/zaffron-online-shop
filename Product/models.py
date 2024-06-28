from django.db import models

from django.utils import timezone


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='Poduct_app/category',default=True,null=True)
    create_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name


class Specifications(models.Model):
    product_id = models.CharField(max_length=50)
    weight = models.FloatField()
    used_for = models.CharField(max_length=60)
    multivatins_type = models.CharField(max_length=60,null=True)


    def __str__(self):
        return self.product_id


class Brand(models.Model):
    name = models.CharField(max_length=50,null=True)
    image = models.ImageField(upload_to='Product_app/Brand',null=True,default=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=40)
    price = models.BigIntegerField()
    score = models.IntegerField()
    image = models.ImageField(upload_to='Product_app/Product',null=True,default=True)
    off_price = models.CharField(max_length=20,null=True)
    descriptions = models.TextField()
    specifications = models.ForeignKey(Specifications,on_delete=models.CASCADE)
    Brand = models.ForeignKey(Brand,on_delete=models.CASCADE)



    def __str__(self):
        return f'{self.name}-{self.price}'