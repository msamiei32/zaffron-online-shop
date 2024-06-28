from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.db import models
from django.urls import reverse
# from .managers import profile

# class manager(models.Manager):
#     def get_queryset(self):
#         return super(manager,self).get_queryset().all()


class CoustomManager(BaseUserManager):

    def create_user(self, phone, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not phone:
            raise ValueError("User must have an phone")

        user = self.model(
            phone=self.normalize_email(phone),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            phone,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    phone = models.CharField(max_length=12,unique=True,verbose_name='تلفن')
    image = models.ImageField(upload_to='account/profile',null=True,verbose_name='تصویر پروفایل')
    username = models.CharField(max_length=150,null=True,default=None,help_text=("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),)
    # objects = profile

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']



    def __str__(self):
        return self.phone

    def get_absolute_url(self):
        return reverse('account:users')


    objects = CoustomManager()







