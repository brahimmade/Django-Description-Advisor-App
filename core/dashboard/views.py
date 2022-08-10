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


class DescriptionView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/description_mgmt.html'

class AboutDescriptionView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/about_description_mgmt.html'

class SkillView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/skill_mgmt.html'

class JobTitleView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/job_title_mgmt.html'

