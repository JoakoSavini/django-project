from django import forms

from products.models import Product

class ProductForms(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'price', 'stock']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class':'form-control', 
                }
            )
        }