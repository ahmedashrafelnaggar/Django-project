from django.urls import path
from.import views

urlpatterns = [
    path('product',views.Product,  name='product'),
    path('', views.products,  name='Products'),

]