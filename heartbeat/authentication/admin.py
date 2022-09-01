from django.contrib import admin
from .models import User, Customer, BloodBank

 # Register your models here.
admin.site.register((User, Customer, BloodBank))

admin.site.site_header  =  "Heartbeat Adminstration"  
admin.site.site_title  =  "Heartbeat"
admin.site.index_title  =  "Heartbeat"