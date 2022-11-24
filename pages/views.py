from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def homePage(request):
    return render(request,'index.html')

def response(request):
    return JsonResponse({'message': 'Hello World!!'})
