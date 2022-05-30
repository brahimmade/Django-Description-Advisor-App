from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.core.paginator import Paginator

from .models import Description
from .forms import DescriptionForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def descriptionList(request,):
    descriptions_query = Description.objects.all().order_by('created_date')
    page = request.GET.get('page', 1)
    
    if request.GET.get("q",None):
        descriptions_query = descriptions_query.filter(text__icontains=request.GET.get("q"))
        
    if request.GET.get("title",None):
        descriptions_query = descriptions_query.filter(job_title__name__icontains=request.GET.get("title"))

    paginator = Paginator(descriptions_query, 2)
    
    try:
        descriptions_query = paginator.page(page)
    except PageNotAnInteger:
        descriptions_query = paginator.page(1)
    except EmptyPage:
        descriptions_query = paginator.page(paginator.num_pages)
    context = {
        "object_list":descriptions_query
    }
    return render(request,'description_list.html',context=context)


def descriptionDetail(request,id):
    description_query = Description.objects.get(id=id)
    context = {
        "object_detail":description_query
    }
    return render(request,'description_detail.html',context=context)

def descriptionEdit(request,id):
    description_obj = Description.objects.get(id=id)
    form_obj = DescriptionForm(instance=description_obj)
    if request.method == 'POST':
        form_obj = DescriptionForm(instance=description_obj,data=request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return HttpResponseRedirect(reverse('advisor:description-list'))
    context = {
        "form":form_obj
    }
    return render(request,'description_edit.html',context=context)
    

def descriptionCreate(request):
    form_obj = DescriptionForm()
    if request.method == 'POST':
        form_obj = DescriptionForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return HttpResponseRedirect(reverse('advisor:description-list'))
    context= {'form':form_obj}
    return render(request,'description_create.html',context=context)

def descriptionDelete(request,id):
    description_obj = Description.objects.get(id=id)
    description_obj.delete()
    return HttpResponseRedirect(reverse('advisor:description-list'))