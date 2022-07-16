from django import forms
from .models import IceCream


class AddIceCreamForm(forms.ModelForm):
    class Meta:
        model = IceCream
        fields = ['name', 'description', 'photo', 'category', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }
