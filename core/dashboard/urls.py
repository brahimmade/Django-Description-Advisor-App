from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "dashboard"

urlpatterns = [
    path("",views.DashboardIndex.as_view(),name="index"),
    path("description/",views.DescriptionView.as_view(),name="description-view"),
    path("skill/",views.SkillView.as_view(),name="skill-view"),
    path("job-title/",views.JobTitleView.as_view(),name="job-title-view"),
    
    # skill urls
    # path("skill/",views.SkillListView.as_view(),name="skill-list"),
    # path("skill/create/",views.SkillCreateView.as_view(),name="skill-create"),
    # path("skill/<int:pk>/",views.SkillDetailView.as_view(),name="skill-detail"),
    # path("skill/<int:pk>/edit/",views.SkillEditView.as_view(),name="skill-edit"),
    # path("skill/<int:pk>/delete/",views.SkillDeleteView.as_view(),name="skill-delete"),
    # path("skill/<int:pk>/archive/",views.SkillArchiveView.as_view(),name="skill-archive"),
    
    # description urls
    # path("description/",views.DescriptionListView.as_view(),name="description-list"),
    # path("description/create/",views.DescriptionCreateView.as_view(),name="description-create"),
    # path("description/<int:pk>/edit/",views.DescriptionEditView.as_view(),name="description-edit"),
    # path("description/<int:pk>/delete/",views.DescriptionDeleteView.as_view(),name="description-delete"),
    # path("description/<int:pk>/archive/",views.DescriptionArchiveView.as_view(),name="description-archive"),
    
    
    # jobs urls
    # path("job-title/",views.JobTitleListView.as_view(),name="job-title-list"),
    # path("job-title/create/",views.JobTitleCreateView.as_view(),name="job-title-create"),
    # path("job-title/<int:pk>/edit/",views.JobTitleEditView.as_view(),name="job-title-edit"),
    # path("job-title/<int:pk>/delete/",views.JobTitleDeleteView.as_view(),name="job-title-delete"),
    # path("job-title/<int:pk>/archive/",views.JobTitleArchiveView.as_view(),name="job-title-archive"),
    
    
    path("api/v1/",include('dashboard.api.v1.urls')),
]

