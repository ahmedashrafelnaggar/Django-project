from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):

    x=[
        ('phones','phones'),
        ('cars','cars')
    ]

    name=models.CharField(max_length=50)
    content=models.TextField(null=True , blank=True, verbose_name='Description')
    price=models.DecimalField(max_digits=5,decimal_places=2)
    image=models.ImageField(upload_to='photos/%y/%m/%d',verbose_name='photo')
    active=models.BooleanField(default=True)
    category=models.CharField(max_length=50, null=True , blank=True,choices=x)

    def __str__(self):
        return self.name
    
    class Meta:
        # verbose_name='المنتجات'
        ordering=['name']



# class test(models.Model):

#     Date=models.DateField()
#     time=models.TimeField()
    # datetime=models.DateTimeField(default=datetime.now)
