from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, UpdateView, TemplateView, CreateView, DeleteView, FormView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from .models import Description, Skill, JobTitle
from .forms import *
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
# Create your views here.


class DashboardIndex(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'


@method_decorator(cache_page(30), name='dispatch')
class SkillListView(ListView):
    queryset = Skill.objects.filter(is_archived=False)
    template_name = 'dashboard/skill_list.html'
    # paginate_by = 3


class SkillCreateView(LoginRequiredMixin, CreateView):
    queryset = Skill.objects.all()
    template_name = 'dashboard/skill_create.html'
    fields = ['name', 'job_title']

    def get_success_url(self):
        return reverse('dashboard:skill-list', kwargs={})

    def form_valid(self, form):
        form.instance.is_core = False
        return super().form_valid(form)


class SkillDetailView(LoginRequiredMixin, DetailView):
    queryset = Skill.objects.all()
    template_name = 'dashboard/skill_detail.html'


class SkillEditView(LoginRequiredMixin, UpdateView):
    queryset = Skill.objects.all()
    template_name = 'dashboard/skill_edit.html'
    form_class = SkillForm
    # fields = ['name', 'job_title']

    def get_success_url(self):
        return reverse('dashboard:skill-list', kwargs={})


class SkillDeleteView(LoginRequiredMixin, DeleteView):
    queryset = Skill.objects.filter(is_core=False)
    template_name = 'dashboard/skill_delete.html'

    def get_success_url(self):
        return reverse('dashboard:skill-list', kwargs={})


@method_decorator(cache_page(30), name='dispatch')
class DescriptionListView(ListView):
    queryset = Description.objects.all()
    template_name = 'dashboard/description_list.html'
    # paginate_by = 3


class DescriptionCreateView(LoginRequiredMixin, CreateView):
    queryset = Description.objects.all()
    template_name = 'dashboard/description_create.html'
    # fields = ['job_title', 'text']
    form_class = DescriptionForm

    def get_success_url(self):
        return reverse('dashboard:description-list', kwargs={})

    def form_valid(self, form):
        form.instance.is_core = False
        return super().form_valid(form)


class DescriptionDetailView(LoginRequiredMixin, DetailView):
    queryset = Description.objects.all()
    template_name = 'dashboard/description_detail.html'


class DescriptionEditView(LoginRequiredMixin, UpdateView):
    queryset = Description.objects.all()
    template_name = 'dashboard/description_edit.html'
    # fields = ['job_title', 'text']
    form_class = DescriptionForm

    def get_success_url(self):
        return reverse('dashboard:description-list', kwargs={})


class DescriptionDeleteView(LoginRequiredMixin, DeleteView):
    queryset = Description.objects.filter(is_core=False)
    template_name = 'dashboard/skill_delete.html'

    def get_success_url(self):
        return reverse('dashboard:description-list', kwargs={})


@method_decorator(cache_page(30), name='dispatch')
class JobTitleListView(ListView):
    queryset = JobTitle.objects.all()
    template_name = 'dashboard/job_title_list.html'


class JobTitleCreateView(LoginRequiredMixin, CreateView):
    queryset = JobTitle.objects.all()
    template_name = 'dashboard/job_title_create.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('dashboard:job-title-list', kwargs={})

    def form_valid(self, form):
        form.instance.is_core = False
        return super().form_valid(form)


class JobTitleEditView(LoginRequiredMixin, UpdateView):
    queryset = JobTitle.objects.all()
    template_name = 'dashboard/job_title_edit.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('dashboard:job-title-list', kwargs={})


class JobTitleDeleteView(LoginRequiredMixin, DeleteView):
    queryset = JobTitle.objects.filter(is_core=False)
    template_name = 'dashboard/job_title_delete.html'

    def get_success_url(self):
        return reverse('dashboard:job-title-list', kwargs={})


class SkillArchiveView(LoginRequiredMixin, FormView):
    template_name = 'dashboard/skill_archive.html'
    form_class = SkillArchiveForm

    def get_success_url(self):
        return reverse('dashboard:skill-list', kwargs={})

    def form_valid(self, form):
        skill_obj = get_object_or_404(Skill,pk=self.kwargs.get('pk',None))
        skill_obj.is_archived = True
        skill_obj.save()
        return super().form_valid(form)


class DescriptionArchiveView(LoginRequiredMixin, FormView):
    template_name = 'dashboard/skill_archive.html'
    form_class = DescriptionArchiveForm

    def get_success_url(self):
        return reverse('dashboard:skill-list', kwargs={})

    def form_valid(self, form):
        description_obj = get_object_or_404(Description,pk=self.kwargs.get('pk',None))
        description_obj.is_archived = True
        description_obj.save()
        return super().form_valid(form)



class JobTitleArchiveView(LoginRequiredMixin, FormView):
    template_name = 'dashboard/skill_archive.html'
    form_class = JobTitleArchiveForm

    def get_success_url(self):
        return reverse('dashboard:job-title-list', kwargs={})

    def form_valid(self, form):
        jobtittle_obj = get_object_or_404(JobTitle,pk=self.kwargs.get('pk',None))
        jobtittle_obj.is_archived = True
        jobtittle_obj.save()
        return super().form_valid(form)
    
