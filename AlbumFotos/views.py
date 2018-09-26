from django.shortcuts import render
from django.http import HttpResponse
from AlbumFotos.models import Categoria, Foto 
from django.views.generic import ListView, DetailView 
from django.shortcuts import render 
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView 

# Create your views here.

def Primera_vista(request):
    return HttpResponse('Esta es mi primera vista!') 

def categoria(request):
    categoria_list = Categoria.objects.all()
    context = {'object_list': categoria_list}
    return render(request, 'AlbumFotos/categoria.html', context)

def categoria_detalles(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    context = {'object': categoria}
    return render(request, 'AlbumFotos/categoria_detail.html', context)

class FotoListView(ListView):
    model = Foto
class FotoDetailView(DetailView):
    model = Foto    

def base(request):
     return render(request, 'base.html')

class FotoUpdate(UpdateView):
    model = Foto
    fields = "__all__"
class FotoCreate(CreateView):
    model = Foto
    fields = "__all__"
class FotoDelete(DeleteView):
    model = Foto
    success_url = reverse_lazy('foto-list')

#class CategoriaCreate(CreateView):
#    model = Categoria
#    fields = "__all__"
