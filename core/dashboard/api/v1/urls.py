from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "api-v1"

urlpatterns = [
    path("skill/",views.SkillListCreateView.as_view(),name="skill-list-create"),
    path("skill/<int:pk>/",views.SkillDetailView.as_view(),name="skill-detail"),
    path("skill/archive/",views.SkillArchiveView.as_view(),name="skill-archive"),
    
    path("job-title/",views.JobTitleListCreateView.as_view(),name="job-title-list-create"),
    path("job-title/<int:pk>/",views.JobTitleDetailView.as_view(),name="job-title-detail"),
    # path("job-title/archive/",views.JobTitleArchiveView.as_view(),name="job-title-archive"),
    
    path("description/",views.DescriptionListCreateView.as_view(),name="description-list-create"),
    path("description/<int:pk>/",views.DescriptionDetailView.as_view(),name="description-detail"),
]