from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.core.paginator import Paginator
from django.views.generic import ListView ,DetailView ,UpdateView,TemplateView

from .models import Description,Skill
from .forms import DescriptionForm

# Create your views here.

class DashboardHome(TemplateView):
    pass


class SkillList(ListView):
    queryset = Skill.objects.all()
    template_name = 'skill_list.html'
    paginate_by = 3


class SkillDetail(DetailView):
    queryset = Skill.objects.all()
    template_name = 'skill_detail.html'

class SkillEdit(UpdateView):
    queryset = Skill.objects.all()
    template_name = 'skill_edit.html'
    fields = '__all__'
    
    def get_success_url(self):
        return reverse('dashboard:skill-list', kwargs={})