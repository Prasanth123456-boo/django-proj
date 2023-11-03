from django.shortcuts import render ,redirect
from django.http import HttpResponse
from . models import movie1

def sample(request):
   
    return render(request,'index.html')

def view(request):
    movie = movie1.objects.all()
    return render(request,"view.html",{'mov':movie})

def create(request):
    if request.POST:
        name = request.POST.get("name")
        age = request.POST.get("age")
        movieobj = movie1(name = name,age = age)
        movieobj.save()
    return render(request,"create.html")

def viewbyid(request,id):
    movieid = movie1.objects.get(id = id)
    return render(request,'viwid.html',{"movieid":movieid})

def edit(request, id):
    movie = movie1.objects.get(id=id)
    
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        
        movie.name = name
        movie.age = age
        movie.save()
        return redirect('view')  # Redirect to the list view after editing
        
    return render(request, 'edit.html', {'movie': movie})

def delete(request, id):
    movie = movie1.objects.get(id=id)
    
    if request.method == "POST":
        movie.delete()
        return redirect('view')  # Redirect to the list view after deletion
        
    return render(request, 'delete.html', {'movie': movie})