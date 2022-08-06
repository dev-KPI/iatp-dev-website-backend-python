from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from api.serializers import MemberSerializer, ProjectSerializer, LanguageSerializer
from api.models import Member, Project, Language

from django_filters.rest_framework import DjangoFilterBackend


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['programming_language', ]
    search_fields = ['last_name', ]


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
