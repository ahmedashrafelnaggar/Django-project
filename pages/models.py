from django.db import models
# from datetime import datetime

# Create your models here.

# class female(models.Model):
#     name_female=models.CharField(max_length=50,null=True)



#     def __str__(self) :
#         return self.name_female


# class male(models.Model):

#     name_male=models.CharField(max_length=50,null=True)
#     girls=models.OneToOneField(female , on_delete=models.CASCADE)


#     def __str__(self) :
#         return self.name_male


# # جدول علاقة بين واحدبكثير 
# class Product(models.Model):
#     title=models.CharField(max_length=50,null=True)

#     def __str__(self) :
#         return self.title

# class user(models.Model):
#     name=models.CharField(max_length=50,null=True)
#     products=models.ForeignKey(Product,on_delete=models.CASCADE)

#     def __str__(self) :
#         return self.name

# # جدول علاقة بين  كثير بكثير 
# class vedio(models.Model):
#     title=models.CharField(max_length=50,null=True)

#     def __str__(self) :
#         return self.title

# class watcher (models.Model):
#     name=models.CharField(max_length=50,null=True)
#     watch=models.ManyToManyField(vedio,related_name='watch')

#     def __str__(self) :
#         return self.name

class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self) :
        return self.username
class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self) :
        return self.name

class Book(models.Model):

    status_book=[

        ('available','available'),
        ('rental','rental'),
        ('sold','sold'),
    
    ]
       


    title=models.CharField(max_length=50)
    image_book=models.ImageField(upload_to='photos/%y/%m/%d', null=True,blank=True)
    author=models.CharField(max_length=50,null=True, blank=True)
    photo_author=models.ImageField(upload_to='photos/%y/%m/%d', null=True,blank=True)
    pages=models.IntegerField(null=True,blank=True)
    price=models.DecimalField(max_digits=5,decimal_places=3,null=True, blank=True)
    retal_price_day=models.DecimalField(max_digits=5,decimal_places=3,null=True, blank=True)
    retal_period=models.IntegerField(null=True,blank=True)
    active=models.BooleanField(default=True)
    status=models.CharField(max_length=50, choices= status_book,null=True, blank=True)
    Category=models.ForeignKey(Category,on_delete=models.PROTECT)


    def __str__(self):
        return self.title


