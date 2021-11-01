from django.shortcuts import render
from django.middleware import csrf
# Create your views here.


def mainView(request):
    csrf.get_token(request)
    return render(request, 'base.html')