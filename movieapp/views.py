from django.http import HttpResponse
from django.shortcuts import render,redirect

from movieapp.forms import Movieform
from movieapp.models import Movie


# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context ={
        'movielist':movie
    }
    return render(request,'index.html', context)
def detail(request,movie_id):
    movie = Movie.objects.get(id = movie_id)
    return render(request,'detail.html',{'movie':movie})

def add(request):
     if request.method == 'POST':
         name= request.POST.get('name')
         description = request.POST.get('description')
         year = request.POST.get('year')
         image = request.FILES['image']
         movie = Movie(name=name,description=description,year=year,image=image)
         movie.save()
     return  render(request,'add.html')


def update(request,id):
    movie = Movie.objects.get(id=id)
    form=Movieform(request.POST or None,request.FILES,instance=movie)
    context = {'form':form,'movie':movie}
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',context)

def delete(request,id):
    if request.method=='POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
