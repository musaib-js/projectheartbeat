from tabnanny import verbose
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe

#Abstract User Model
class User(AbstractUser):
    is_bloodbank = models.BooleanField('Blood Bank Status', default=False)
    is_customer = models.BooleanField('Customer Status', default=False)

#User Model
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length = 350, default = "Customer")
    age = models.IntegerField(default = 00)
    gender = models.CharField(max_length=6, default = "not-specfied")
    location = models.CharField(max_length=600, default="none")
    contact = models.CharField(max_length = 13)
    photo = models.ImageField(upload_to = 'media', default = 'one.jpg')

    def __str__(self):
        return self.name

#Blood Bank Model
class BloodBank(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=250, default = "Bank Name")
    contact = models.CharField(max_length = 13)
    email = models.EmailField(max_length = 200)
    location = models.CharField(max_length=600, default="none")
    owner_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Blood Banks" 