from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from django.http import HttpResponse
from carros.forms import CarroForm
from carros.models import Carro
from django.core.paginator import Paginator
# Create your views here.

def home(request):
   data={}
   search = request.GET.get('search')
   if search:
      data['db'] = Carro.objects.filter(carro__icontains=search)
   else :  
      data['db'] = Carro.objects.all()
   '''
   all = Carro.objects.all()
   paginator = Paginator(all, 2)
   pages = request.GET.get('page')
   data['db'] = paginator.get_page(pages)
   '''   
   return render(request, 'home.html', data)
   
def form(request):
   data={}
   data["form"]=CarroForm()
   return render(request,'form.html',data)

def view(request, pk):
   data={}
   data['db'] = Carro.objects.get(pk=pk)
   return render(request, 'view.html', data)  

def create(request):
   form = CarroForm(request.POST or None)
   if form.is_valid():
      form.save()
      return redirect('home') 

def edit(request, pk):
   data={}
   data['db']= Carro.objects.get(pk=pk)
   data['form']= CarroForm(instance=data['db'])
   return render(request,'form.html', data)

def update(request, pk):
   data={}
   data['db']= Carro.objects.get(pk=pk)
   form = CarroForm(request.POST or None, instance=data['db'])
   if form.is_valid():
      form.save()
      return redirect('home')
   
   
def delete(request, pk):
   db = Carro.objects.get(pk=pk)
   db.delete()
   return redirect('home')   

