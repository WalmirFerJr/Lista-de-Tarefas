from django.http import HttpResponse

def teste_view(request):
    return HttpResponse("Rota teste")

def index_view(request):
    return HttpResponse("Página inicial")