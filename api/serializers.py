from rest_framework import serializers

from api.models import (
    Member,
    Project,
    Language,
    Specialization,
    SocialLinks,
    GitHubLinks,
)


class MemberCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"


class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class SocialLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = "__all__"


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = "__all__"


class GitHubLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = GitHubLinks
        fields = "__all__"


class GitHubLinksforSerializer(serializers.ModelSerializer):
    class Meta:
        model = GitHubLinks
        fields = ["id", "title", "link"]


class SocialLinksforMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = ["id", "social_link", "link"]


class ProjectsforMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "title"]


class MemberDetailSerializer(serializers.ModelSerializer):
    specialization = serializers.StringRelatedField(many=True)
    programming_language = serializers.StringRelatedField(many=True)
    social_links = SocialLinksforMemberSerializer(many=True)
    projects = ProjectsforMemberSerializer(many=True)

    counter_projects = serializers.SerializerMethodField("count")

    def count(self, member):
        member_id = member.id
        return len(Project.objects.filter(members=member_id).values())

    class Meta:
        model = Member
        fields = [
            "id",
            "photo_url",
            "first_name",
            "last_name",
            "date_of_birth",
            "summary",
            "programming_language",
            "specialization",
            "email",
            "social_links",
            "projects",
            "counter_projects",
        ]


class ProjectDetailSerializer(serializers.ModelSerializer):
    specialization = serializers.StringRelatedField(many=True)
    programming_language = serializers.StringRelatedField(many=True)
    members = serializers.StringRelatedField(many=True)
    github_links = GitHubLinksforSerializer(many=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "photo_url",
            "title",
            "description",
            "members",
            "specialization",
            "programming_language",
            "github_links",
        ]
