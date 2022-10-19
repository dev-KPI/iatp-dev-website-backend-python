from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from api.serializers import (
    MemberDetailSerializer,
    ProjectDetailSerializer,
    LanguageSerializer,
    SpecializationSerializer,
    SocialLinksSerializer,
    MemberCreateSerializer,
    ProjectCreateSerializer,
    GitHubLinksSerializer,
)
from api.models import (
    Member,
    Project,
    Language,
    Specialization,
    SocialLinks,
    GitHubLinks,
)


class MemberCreateViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Member.objects.all()
    serializer_class = MemberCreateSerializer


class ProjectCreateViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class SpecializationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class GitHubLinksViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = GitHubLinks.objects.all()
    serializer_class = GitHubLinksSerializer


class SocialLinksViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
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
