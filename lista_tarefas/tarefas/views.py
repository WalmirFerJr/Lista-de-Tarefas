from django.shortcuts import render
from .forms import TarefaForm
from django.http import HttpRequest
from django.shortcuts import redirect
from .models import TarefaModel
# Create your views here.

def tarefas_home(request):
    contexto = {
        "nome": "Walmir",
        "tarefas":TarefaModel.objects.all()
    }
    return render(request, 'tarefas/home.html', contexto)
    
def tarefas_adicionar(request:HttpRequest):
    if request.method == "POST":
        formulario = TarefaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("tarefas:home")
            
    contexto = {
        "form":TarefaForm
    }
    return render(request, 'tarefas/adicionar.html', contexto)

