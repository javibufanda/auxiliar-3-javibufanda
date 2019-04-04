from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'Paginajavi/index.html')

def index2(request):
	return render(request, 'Paginajavi/index2.html')

def cuerpodocente(request):
	return render(request, 'Paginajavi/cuerpodocente.html')