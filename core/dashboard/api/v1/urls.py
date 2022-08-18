from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "api-v1"

urlpatterns = [
    path("skill/",views.SkillListCreateView.as_view(),name="skill-list-create"),
    path("skill/<int:pk>/",views.SkillDetailView.as_view(),name="skill-detail"),
    path("skill/archive/",views.SkillArchiveView.as_view(),name="skill-archive"),
    path("skill/mark/",views.SkillMarkView.as_view(),name="skill-mark"),
    path("skill/calculate-relation/",views.SkillRelationCalculateView.as_view(),name="skill-calculation"),
    path("skill/multi-select/action/",views.SkillMultiSelectAction.as_view(),name="skill-multi-select-action"),
    
    
    path("job-title/",views.JobTitleListCreateView.as_view(),name="job-title-list-create"),
    path("job-title/all/",views.JobTitleAllView.as_view(),name="job-title-all"),
    path("job-title/<int:pk>/",views.JobTitleDetailView.as_view(),name="job-title-detail"),
    path("job-title/archive/",views.JobTitleArchiveView.as_view(),name="job-title-archive"),
    path("job-title/mark/",views.JobTitleMarkView.as_view(),name="job-title-mark"),
    path("job-title/calculate-relation/",views.JobTitleRelationCalculateView.as_view(),name="job-title-calculation"),
    path("job-title/multi-select/action/",views.JobTitleMultiSelectAction.as_view(),name="job-title-multi-select-action"),
    
    path("description/",views.DescriptionListCreateView.as_view(),name="description-list-create"),
    path("description/<int:pk>/",views.DescriptionDetailView.as_view(),name="description-detail"),
    path("description/archive/",views.DescriptionArchiveView.as_view(),name="description-archive"),
    path("description/mark/",views.DescriptionMarkView.as_view(),name="description-archive"),
    path("description/calculate-relation/",views.DescriptionRelationCalculateView.as_view(),name="description-calculation"),
    path("description/multi-select/action/",views.DescriptionMultiSelectAction.as_view(),name="description-multi-select-action"),
    
    path("description-about/",views.AboutDescriptionListCreateView.as_view(),name="about-description-list-create"),
    path("description-about/<int:pk>/",views.AboutDescriptionDetailView.as_view(),name="about-description-detail"),
    path("description-about/archive/",views.AboutDescriptionArchiveView.as_view(),name="about-description-archive"),
    path("description-about/mark/",views.AboutDescriptionMarkView.as_view(),name="about-description-archive"),
    path("description-about/calculate-relation/",views.AboutDescriptionRelationCalculateView.as_view(),name="about-description-calculation"),
    path("description-about/multi-select/action/",views.AboutDescriptionMultiSelectAction.as_view(),name="about-description-multi-select-action"),
    
    
    path("skill/out-usage/<str:token>/",views.SkillListOutView.as_view(),name="skill-list-out"),
    path("job-title/out-usage/<str:token>/",views.JobTitleListOutView.as_view(),name="job-title-list-out"),
    path("description/out-usage/<str:token>/",views.DescriptionListOutView.as_view(),name="description-list-out"),
    path("description-about/out-usage/<str:token>/",views.AboutDescriptionListOutView.as_view(),name="about-description-list-out"),
]