from rest_framework import serializers
from api.models import Member, Project, Language, Specialization, SocialLinks


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = "__all__"


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class MemberSerializer(serializers.ModelSerializer):
    specialization = serializers.StringRelatedField(many=True)
    programming_language = serializers.StringRelatedField(many=True)

    class Meta:
        model = Member
        fields = [
            "photo_url",
            "first_name",
            "last_name",
            "date_of_birth",
            "summary",
            "programming_language",
            "specialization",
            "email",
        ]


class ProjectSerializer(serializers.ModelSerializer):
    specialization = serializers.StringRelatedField(many=True)
    programming_language = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "members",
            "github_project",
            "specialization",
            "programming_language",
        ]


class SocialLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = "__all__"
