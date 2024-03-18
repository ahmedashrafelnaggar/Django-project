from django import forms
from . models import Book,Category


# class Loginform(forms.ModelForm):
#     class Meta:
#         model=Login
#         fields='__all__'

class Categoryform(forms.ModelForm):
    class Meta:
        model=Category
        fields=[
            'name',
        ]

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
        },

class Bookform(forms.ModelForm):
    class Meta:
        model=Book
        # fields='__all__'     

        # if you need part not all 
        fields=['title',
                'author',
                'price',
                'Category',
                'photo_author'
                

                ]
        
        # widgets like css but for forms only 
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
             'photo_author':forms.FileInput(attrs={'class':'form-control'}),
        }