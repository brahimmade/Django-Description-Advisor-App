from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "api-v1"

urlpatterns = [
    path("skill/",views.SkillListCreateView.as_view(),name="skill-list-create"),
    path("skill/<int:pk>/",views.SkillDetailView.as_view(),name="skill-detail"),
    path("skill/archive/",views.SkillArchiveView.as_view(),name="skill-archive"),
]