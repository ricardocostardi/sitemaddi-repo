from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.
def produtos(request):
	return render(request, 'produtosapp/produtos.html')