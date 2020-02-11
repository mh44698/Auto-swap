from django import forms
from .models import Car, Seller

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ('make','model', 'trim', 'img_url','milage', 'color','name')

class SellerForm(forms.ModelForm):

    class Meta:
        model = Seller
        fields = ('name', 'phone', 'address','web_site')