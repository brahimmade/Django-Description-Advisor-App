from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "dashboard"

urlpatterns = [
    path("",views.DashboardHome.as_view(),name="home"),

    path("skill/",views.SkillList.as_view(),name="skill-list"),
    path("skill/<int:pk>/",views.SkillDetail.as_view(),name="skill-detail"),
    path("skill/<int:pk>/edit/",views.SkillEdit.as_view(),name="skill-edit"),
]

