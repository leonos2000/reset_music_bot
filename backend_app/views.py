from django.shortcuts import render
from django.middleware import csrf
from django.http import JsonResponse
# Create your views here.
import os

def mainView(request):
    csrf.get_token(request)
    return render(request, 'base.html')

def rebootView(request):
    if request.method == 'POST':
        if request.POST.get('password') == 'ZmartwychwstajCzarodzieju':
            os.system('whoami > /srv/test')
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'})