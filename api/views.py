from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from api.serializers import (
    MemberDetailSerializer,
    ProjectDetailSerializer,
    LanguageSerializer,
    SpecializationSerializer,
    SocialLinksSerializer,
    MemberCreateSerializer,
    ProjectCreateSerializer,
)
from api.models import Member, Project, Language, Specialization, SocialLinks


class MemberCreateViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberCreateSerializer


class ProjectCreateViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class SocialLinksViewSet(viewsets.ModelViewSet):
    queryset = SocialLinks.objects.all()
    serializer_class = SocialLinksSerializer


class MemberDetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberDetailSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["programming_language", "specialization"]
    search_fields = [
        "last_name",
    ]


class ProjectDetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["members", "specialization"]
    search_fields = ["title"]
