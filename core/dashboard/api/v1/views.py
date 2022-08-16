
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
from .thread_task import SkillCalculationThread ,DescriptionCalculationThread,JobCalculationThread,AboutDescriptionCalculationThread

class SkillListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SkillSerializer
    queryset = Skill.objects.filter()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {'job_title': ["exact"],'is_archived':["exact"]}
    search_fields = ["name", 'id']
    ordering_fields = ["created_date", 'name', 'id', 'related_job_titles']
    pagination_class = DefaultPagination

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data['total_marks'] = (
            self.get_queryset()).filter(is_marked=True).count()
        return response


class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ getting detail of the post and edit plus removing it """
    permission_classes = [IsAuthenticated]
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()

    def destroy(self, request, *args, **kwargs):
        object = self.get_object()
        if (object.is_core or request.user.is_superuser) and object.is_core:
            return Response({"detail": "you are not allowed to remove core objects instead archive them"}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)


class SkillArchiveView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SkillArchiveSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        skill_obj = serializer.validated_data['skill_obj']
        if skill_obj.is_archived:
            operation = 'unarchived'
            skill_obj.is_archived = False
            skill_obj.save()
        else:
            operation = 'archived'
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
    queryset = JobTitle.objects.filter()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {'is_archived':['exact']}
    search_fields = ["name", 'id']
    ordering_fields = ["created_date", 'name', 'id',
                       'related_descriptions', 'related_skills']
    pagination_class = DefaultPagination

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data['total_marks'] = (
            self.get_queryset()).filter(is_marked=True).count()
        return response


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
        if (object.is_core or request.user.is_superuser) and object.is_core:
            return Response({"detail": "you are not allowed to remove core objects instead archive them"}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)


class JobTitleArchiveView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JobTitleArchiveSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        job_title_obj = serializer.validated_data['job_title_obj']
        if job_title_obj.is_archived:
            operation = 'unarchive'
            job_title_obj.is_archived = False
            job_title_obj.save()
        else:
            operation = 'archive'
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
    queryset = Description.objects.filter()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {'job_title': {'exact'},'is_archived':['exact']}
    search_fields = ["text", 'id']
    ordering_fields = ["created_date", 'id', 'related_job_titles']
    pagination_class = DefaultPagination

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data['total_marks'] = (
            self.get_queryset()).filter(is_marked=True).count()
        return response


class DescriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ getting detail of the post and edit plus removing it """
    permission_classes = [IsAuthenticated]
    serializer_class = DescriptionSerializer
    queryset = Description.objects.all()

    def destroy(self, request, *args, **kwargs):
        object = self.get_object()
        if (object.is_core or request.user.is_superuser) and object.is_core:
            return Response({"detail": "you are not allowed to remove core objects instead archive them"}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)


class DescriptionArchiveView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DescriptionArchiveSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        description_obj = serializer.validated_data['description_obj']
        if description_obj.is_archived:
            operation = 'unarchived'
            description_obj.is_archived = False
            description_obj.save()
        else:
            operation = 'archived'
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


class SkillRelationCalculateView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        skill_query = Skill.objects.filter(is_archived=False)
        SkillCalculationThread(skill_query).start()        
        return Response({"detail": "relations are being process, it may take approximately 2 minute."}, status=status.HTTP_201_CREATED)


class JobTitleRelationCalculateView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        description_query = Description.objects.filter(is_archived=False)
        skill_query = Skill.objects.filter(is_archived=False)
        job_title_query = JobTitle.objects.filter(is_archived=False)
        about_query = AboutDescription.objects.filter(is_archived=False)
        JobCalculationThread(skill_query,description_query,job_title_query,about_query).start() 
        

        return Response({"detail": "relations are being process, it may take approximately 2 minute."}, status=status.HTTP_201_CREATED)


class DescriptionRelationCalculateView(views.APIView):
    def post(self, request, *args, **kwargs):
        description_query = Description.objects.filter(is_archived=False)
        DescriptionCalculationThread(description_query).start()  
        return Response({"detail": "relations are being process, it may take approximately 2 minute."}, status=status.HTTP_201_CREATED)


def mark_objects(Model, list_id):
    failed_objects = 0
    for id in list_id:
        try:
            object = Model.objects.get(id=id)
            object.is_marked = True
            object.save()
        except:
            failed_objects += 1
    return failed_objects


def unmark_objects(Model, list_id):
    failed_objects = 0
    for id in list_id:
        try:
            object = Model.objects.get(id=id)
            object.is_marked = False
            object.save()
        except:
            failed_objects += 1
    return failed_objects


def archive_objects(Model, list_id):
    failed_objects = 0
    for id in list_id:
        try:
            object = Model.objects.get(id=id)
            object.is_archived = True
            object.save()
        except:
            failed_objects += 1
    return failed_objects


def unarchive_objects(Model, list_id):
    failed_objects = 0
    for id in list_id:
        try:
            object = Model.objects.get(id=id)
            object.is_archived = False
            object.save()
        except:
            failed_objects += 1
    return failed_objects


OPT_TYPE = {'mark': (lambda model, list_id: mark_objects(model, list_id)),
            'unmark': (lambda model, list_id: unmark_objects(model, list_id)),
            'archive': (lambda model, list_id: archive_objects(model, list_id)),
            'unarchive': (lambda model, list_id: unarchive_objects(model, list_id))}


class SkillMultiSelectAction(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MultiSelectActionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        list_ids = serializer.validated_data['list_ids']
        operation_type = serializer.validated_data['operation_type']
        operation_function = OPT_TYPE[operation_type]
        failed_objects = operation_function(Skill, list_ids)
        return Response({'detail': f'{operation_type} operation is done on {len(list_ids)} objects and {failed_objects} failed'})


class DescriptionMultiSelectAction(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MultiSelectActionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        list_ids = serializer.validated_data['list_ids']
        operation_type = serializer.validated_data['operation_type']
        operation_function = OPT_TYPE[operation_type]
        failed_objects = operation_function(Description, list_ids)
        return Response({'detail': f'{operation_type} operation is done on {len(list_ids)} objects and {failed_objects} failed'})


class JobTitleMultiSelectAction(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MultiSelectActionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        list_ids = serializer.validated_data['list_ids']
        operation_type = serializer.validated_data['operation_type']
        operation_function = OPT_TYPE[operation_type]
        failed_objects = operation_function(JobTitle, list_ids)
        return Response({'detail': f'{operation_type} operation is done on {len(list_ids)} objects and {failed_objects} failed'})



class AboutDescriptionListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AboutDescriptionSerializer
    queryset = AboutDescription.objects.filter()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {'job_title': {'exact'},'is_archived':['exact']}
    search_fields = ["text", 'id']
    ordering_fields = ["created_date", 'id', 'related_job_titles']
    pagination_class = DefaultPagination

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data['total_marks'] = (
            self.get_queryset()).filter(is_marked=True).count()
        return response


class AboutDescriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ getting detail of the post and edit plus removing it """
    permission_classes = [IsAuthenticated]
    serializer_class = AboutDescriptionSerializer
    queryset = AboutDescription.objects.all()

    def destroy(self, request, *args, **kwargs):
        object = self.get_object()
        if (object.is_core or request.user.is_superuser) and object.is_core:
            return Response({"detail": "you are not allowed to remove core objects instead archive them"}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)


class AboutDescriptionArchiveView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AboutDescriptionArchiveSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        description_obj = serializer.validated_data['description_obj']
        if description_obj.is_archived:
            operation = 'unarchived'
            description_obj.is_archived = False
            description_obj.save()
        else:
            operation = 'archived'
            description_obj.is_archived = True
            description_obj.save()
        return Response({"detail": f"description object {description_obj.id} archived successfully"}, status=status.HTTP_202_ACCEPTED)


class AboutDescriptionMarkView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AboutDescriptionMarkSerializer

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
    
    
class AboutDescriptionMultiSelectAction(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MultiSelectActionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        list_ids = serializer.validated_data['list_ids']
        operation_type = serializer.validated_data['operation_type']
        operation_function = OPT_TYPE[operation_type]
        failed_objects = operation_function(AboutDescription, list_ids)
        return Response({'detail': f'{operation_type} operation is done on {len(list_ids)} objects and {failed_objects} failed'})
    

class AboutDescriptionRelationCalculateView(views.APIView):
    def post(self, request, *args, **kwargs):
        description_query = AboutDescription.objects.filter(is_archived=False)
        AboutDescriptionCalculationThread(description_query).start()  
        return Response({"detail": "relations are being process, it may take approximately 2 minute."}, status=status.HTTP_201_CREATED)