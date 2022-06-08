
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
        object = self.get_object()
        if ( object.is_core or  request.user.is_superuser) and  object.is_core:
            return Response({"detail": "you are not allowed to remove core objects instead archive them"}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
        

class SkillArchiveView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SkillArchiveSerializer
    
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        skill_obj = serializer.validated_data['skill_obj']
        skill_obj.is_archived = True
        skill_obj.save()
        return Response({"detail": f"skill obj {skill_obj.id} archived successfully"}, status=status.HTTP_202_ACCEPTED)

class SkillMarkView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SkillMarkSerializer
    
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        skill_obj = serializer.validated_data['skill_obj']
        operation = ''
        if skill_obj.is_marked:
            operation = 'unmarked'
            skill_obj.is_marked = False
            skill_obj.save()
        else:
            operation = 'marked'
            skill_obj.is_marked = True
            skill_obj.save()
        
        
        return Response({"detail": f"skill obj {skill_obj.id} {operation} successfully"}, status=status.HTTP_202_ACCEPTED)
    

class JobTitleListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JobTitleSerializer
    queryset = JobTitle.objects.filter(is_archived=False)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {}
    search_fields = ["name"]
    ordering_fields = ["created_date", 'name']
    pagination_class = DefaultPagination

class JobTitleAllView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JobTitleMinimumSerializer
    queryset = JobTitle.objects.filter(is_archived=False)



class JobTitleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ getting detail of the post and edit plus removing it """
    permission_classes = [IsAuthenticated]
    serializer_class = JobTitleSerializer
    queryset = JobTitle.objects.all()

    def destroy(self, request, *args, **kwargs):
        object = self.get_object()
        if ( object.is_core or  request.user.is_superuser) and  object.is_core:
            return Response({"detail": "you are not allowed to remove core objects instead archive them"}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

class JobTitleArchiveView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JobTitleArchiveSerializer
    
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        job_title_obj = serializer.validated_data['job_title_obj']
        job_title_obj.is_archived = True
        job_title_obj.save()
        return Response({"detail": f"job title obj {job_title_obj.id} archived successfully"}, status=status.HTTP_202_ACCEPTED)
    

class JobTitleMarkView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JobTitleMarkSerializer
    
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        job_title_obj = serializer.validated_data['job_title_obj']
        operation = ''
        if job_title_obj.is_marked:
            operation = 'unmarked'
            job_title_obj.is_marked = False
            job_title_obj.save()
        else:
            operation = 'marked'
            job_title_obj.is_marked = True
            job_title_obj.save()
        return Response({"detail": f"description obj {job_title_obj.id} {operation} successfully"}, status=status.HTTP_202_ACCEPTED)

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
        object = self.get_object()
        if ( object.is_core or  request.user.is_superuser) and  object.is_core:
            return Response({"detail": "you are not allowed to remove core objects instead archive them"}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
        
        
class DescriptionArchiveView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DescriptionArchiveSerializer
    
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        description_obj = serializer.validated_data['description_obj']
        description_obj.is_archived = True
        description_obj.save()
        return Response({"detail": f"description object {description_obj.id} archived successfully"}, status=status.HTTP_202_ACCEPTED)
    

class DescriptionMarkView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DescriptionMarkSerializer
    
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        description_obj = serializer.validated_data['description_obj']
        operation = ''
        if description_obj.is_marked:
            operation = 'unmarked'
            description_obj.is_marked = False
            description_obj.save()
        else:
            operation = 'marked'
            description_obj.is_marked = True
            description_obj.save()
        return Response({"detail": f"description object {description_obj.id} {operation} successfully"}, status=status.HTTP_202_ACCEPTED)