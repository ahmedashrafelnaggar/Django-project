from django.urls import path
from.import views



urlpatterns = [
    path('', views.index,  name='index'),
    # path('about', views.about,  name='about'),
    path('update/<int:id>', views.update,  name='update'),
    path('books', views.books,  name='books'),
    path('delete/<int:id>', views.delete,  name='delete'),


]