from django.shortcuts import render,redirect,get_object_or_404
from.models import *
from.forms import Bookform,Categoryform
# from.forms import Loginform




# Create your views here.
def index(request):

    if request.method =='POST':
        dataform=Bookform(request.POST,request.FILES)

        if dataform.is_valid():
             dataform.save()

        data_book=Categoryform(request.POST)
        if data_book.is_valid():
            data_book.save()
        




    context={
        'category':Category.objects.all(),
        'books':Book.objects.all(),
        'form':Bookform(),
        'catform':Categoryform(),
    }
    return render(request, "pages/index.html",context)




# def about(request):
#     if request.method =='POST':
#         dataform=Loginform(request.POST)

#         if dataform.is_valid():
#              dataform.save()


#     return render(request,"pages/about.html", {'pro': Loginform })
    
def update(request , id ):
    book_id=Book.objects.get(id=id)

    if request.method=='post':
        # كده بتقوله دخلي بيانات ال form دي
        # with id
        data_form=Bookform(request.POST,request.FILES,instance=book_id)
        if data_form.is_valid():
            data_form.save()
            return redirect('/')


    else:       
        data_form=Bookform(instance=book_id)

    context={
        
        # 'books':Book.objects.all(),
        'form':data_form,
        
    }


    return render(request, "pages/update.html",context)


def delete(request, id ):
    book_delete=get_object_or_404(Book,id=id)
    if request.method=='post':
        book_delete.delete()
        return redirect('/')
    return render(request, "pages/delete.html")


def books(request):
    context={
        'category':Category.objects.all(),
        'books':Book.objects.all(),
    }
    return render(request, "pages/books.html",context)
    
   
   