from django.contrib import admin

# Register your models here.
from .models import Car, Seller

admin.site.register([Car, Seller])