from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def descriptionList(request):
    
    return render(request,'description_list.html')