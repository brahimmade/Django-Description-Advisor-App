from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "advisor"

urlpatterns = [
    path('description/',views.descriptionList,name="description-list"),
    path('description/create/',views.descriptionCreate,name="description-create"),
    path('description/<int:id>/',views.descriptionDetail,name="description-detail"),
    path('description/<int:id>/edit/',views.descriptionEdit,name="description-edit"),
    path('description/<int:id>/delete/',views.descriptionDelete,name="description-delete")
]

