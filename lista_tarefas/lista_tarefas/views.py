from django.http import HttpResponse
from django.shortcuts import redirect

def teste_view(request):
    return HttpResponse("Rota teste")

def index_view(request):
    return redirect("tarefas:home")