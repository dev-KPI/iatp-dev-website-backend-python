from rest_framework import viewsets

from api.serializers import MemberSerializer, ProjectSerializer
from api.models import Member, Project


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
