from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.
def index(request):
	return render(request, 'siteapp/home.html')

def sobre(request):
	return render(request, 'siteapp/sobre.html')


def contato(request):
	return render(request, 'siteapp/contato.html')		