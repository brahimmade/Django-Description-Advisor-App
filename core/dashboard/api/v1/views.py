
from rest_framework import viewsets, generics, mixins, views
from rest_framework import pagination, status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from ...models import *
from .serializers import *
from .paginations import *


class SkillListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SkillSerializer
    queryset = Skill.objects.filter(is_archived=False)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {'job_title': ["exact"]}
    search_fields = ["name"]
    ordering_fields = ["created_date", 'name']
    pagination_class = DefaultPagination


class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ getting detail of the post and edit plus removing it """
    permission_classes = [IsAuthenticated]
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs) if request.user.is_superuser else Response(
            {"detail": "you are not allowed to remove core objects instead archive them"}, status=status.HTTP_403_FORBIDDEN)
        

class SkillArchiveView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SkillArchiveSerializer
    
    
    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        skill_obj = serializer.validated_data['skill_obj']
        skill_obj.is_archived = True
        skill_obj.save()
        return Response({"detail": f"skill obj {skill_obj.id} archived successfully"}, status=status.HTTP_202_ACCEPTED)
    

class JobTitleListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JobTitleSerializer
    queryset = JobTitle.objects.filter(is_archived=False)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {}
    search_fields = ["name"]
    ordering_fields = ["created_date", 'name']
    pagination_class = DefaultPagination



class JobTitleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ getting detail of the post and edit plus removing it """
    permission_classes = [IsAuthenticated]
    serializer_class = JobTitleSerializer
    queryset = JobTitle.objects.all()

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs) if request.user.is_superuser else Response(
            {"detail": "you are not allowed to remove core objects instead archive them"}, status=status.HTTP_403_FORBIDDEN)
    

class DescriptionListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DescriptionSerializer
    queryset = Description.objects.filter(is_archived=False)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {}
    search_fields = ["text"]
    ordering_fields = ["created_date"]
    pagination_class = DefaultPagination



class DescriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ getting detail of the post and edit plus removing it """
    permission_classes = [IsAuthenticated]
    serializer_class = DescriptionSerializer
    queryset = Description.objects.all()

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs) if request.user.is_superuser else Response(
            {"detail": "you are not allowed to remove core objects instead archive them"}, status=status.HTTP_403_FORBIDDEN)