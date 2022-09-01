from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import BloodBank, User, Customer

class CustomerSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        customer.save()
        return user

class BloodBankSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_bloodbank = True
        if commit:
            user.save()
        bloodbank = BloodBank.objects.create(user=user)
        bloodbank.save()
        return user

class CustomerForm(forms.ModelForm):  
    class Meta:  
        model = Customer
        fields = ['name', 'age', 'gender', 'location', 'contact', 'photo']


class BloodBankForm(forms.ModelForm):  
    class Meta:  
        model = BloodBank
        fields = ['name', 'contact', 'email', 'location', 'owner_name'] 
