from rest_framework import serializers
from api.models import Member, Project, Language, Specialization


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
