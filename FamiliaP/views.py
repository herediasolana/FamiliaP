from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
	return HttpResponse('Primera Pagina')


def despedida(request):
	return HttpResponse('Adios!')

def index(request):
    return render (request, 'index.html')