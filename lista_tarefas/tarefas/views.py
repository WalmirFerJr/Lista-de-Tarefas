from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def tarefas_home(request):
    return HttpResponse("Essa é sua lista de tarefas!")

def tarefas_adicionar(request):
    return HttpResponse("Adicione aqui sua tarefa!")

