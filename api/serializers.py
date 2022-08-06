from rest_framework import serializers
from api.models import Member, Project


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    members = serializers.HyperlinkedIdentityField(view_name="api:members-detail")

    class Meta:
        model = Project
        fields = '__all__'
