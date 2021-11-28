from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#def index(request):
#    return HttpResponse('HelloWorld')

def index(request):

    return render(request, 'portfolio_landing/index.html', context={})

def cv_page(request):

    return render(request, 'portfolio_landing/CV.html', context={})