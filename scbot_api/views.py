from django.shortcuts import render
from rest_framework import viewsets
from .models import Communication, File, Project
from .serializers import CommunicationSerializer, FileSerializer, ProjectSerializer
import uuid
from django.utils import timezone
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()

    def retrieve(self, request, *args, **kwargs):
        projectId = kwargs.get('pk')
        queryset = self.get_queryset().filter(project_id=projectId)
        project = get_object_or_404(queryset, project_id=projectId)
        serializer = self.get_serializer(project)
        return Response(serializer.data)
