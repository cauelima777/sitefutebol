from django import forms
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView, UpdateView, DetailView,DeleteView
from dados.models import Jogador,Dados,Clube
from .forms import DadosForm
from django.shortcuts import render



def pagina_inicial(request):
    return render(request, 'index.html')

class JogadorDetail(DetailView):
    model = Jogador
    template_name = 'jogador_detail.html'
    context_object_name = 'jogador'

class DadosCreate(CreateView): 
    model = Dados
    form_class = DadosForm
    template_name = 'dados/dados_form.html'
    success_url = reverse_lazy('dados:list')

class DadosDeleteView(DeleteView):
    model = Dados
    template_name = 'dados/dados_confirm_delete.html'
    success_url = reverse_lazy('dados:list')




class ClubeCreate(CreateView):
    model = Clube
    fields = ['nome']
    template_name = 'dados/clube_form.html'
    success_url = reverse_lazy('dados:list')


class JogadorList(ListView):
    model = Jogador
    queryset = Jogador.objects.all() 


class JogadorCreate(CreateView): 
    model = Jogador 
    fields = '__all__'
    success_url = reverse_lazy('dados:list')
    
class JogadorUpdate(UpdateView):
    model = Jogador 
    fields = '__all__'
    success_url = reverse_lazy('dados:list')

class JogadorDetail(DetailView): 
    queryset = Jogador.objects.all() 
  


class JogadorDelete(DeleteView):
    queryset = Jogador.objects.all() 
    success_url = reverse_lazy('dados:list')



