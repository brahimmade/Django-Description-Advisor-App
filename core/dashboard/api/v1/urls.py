from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "api-v1"

urlpatterns = [
    path("skill/",views.SkillListCreateView.as_view(),name="skill-list-create"),
    path("skill/<int:pk>/",views.SkillDetailView.as_view(),name="skill-detail"),
    path("skill/archive/",views.SkillArchiveView.as_view(),name="skill-archive"),
    path("skill/mark/",views.SkillMarkView.as_view(),name="skill-mark"),
    
    path("job-title/",views.JobTitleListCreateView.as_view(),name="job-title-list-create"),
    path("job-title/all/",views.JobTitleAllView.as_view(),name="job-title-all"),
    path("job-title/<int:pk>/",views.JobTitleDetailView.as_view(),name="job-title-detail"),
    path("job-title/archive/",views.JobTitleArchiveView.as_view(),name="job-title-archive"),
    path("job-title/mark/",views.JobTitleMarkView.as_view(),name="job-title-mark"),
    
    path("description/",views.DescriptionListCreateView.as_view(),name="description-list-create"),
    path("description/<int:pk>/",views.DescriptionDetailView.as_view(),name="description-detail"),
    path("description/archive/",views.DescriptionArchiveView.as_view(),name="description-archive"),
    path("description/mark/",views.DescriptionMarkView.as_view(),name="description-archive"),
]