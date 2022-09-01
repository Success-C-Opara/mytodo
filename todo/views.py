from multiprocessing import context
from tokenize import Token
from django.shortcuts import render,redirect
from .models import Todomodel

# Create your views here.
def index(request):
    gets  = Todomodel.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')

        submit= Todomodel(title=title)
        submit.save()

    context ={
        'forms':gets
    }
    return render(request, 'todo/home.html',context)





def delete(request,id):
    gex = Todomodel.objects.get(id=id)
    gex.delete()
    return redirect('home')
