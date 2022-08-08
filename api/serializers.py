from rest_framework import serializers
from api.models import Member, Project, Language


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    # language = serializers.HyperlinkedIdentityField(view_name="api:languages-detail")
    # викликає помилку, тому закоментував! Треба з цим розібратись!
    class Meta:
        model = Member
        fields = '__all__'


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    # members = serializers.HyperlinkedIdentityField(view_name="api:members-detail")

    class Meta:
        model = Project
        fields = '__all__'
