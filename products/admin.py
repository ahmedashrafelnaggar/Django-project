from django.contrib import admin
from . models import Product 
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','active']
    list_display_links=['price']
    list_editable=['name','active']
    search_fields=['name']









admin.site.register(Product,ProductAdmin)
# admin.site.register(test)
admin.site.site_header='ahmed ashraf'
admin.site.site_title='ibn el naggar'



