from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Language, Specialization, Member, Project
from api.serializers import (
    LanguageSerializer,
    SpecializationSerializer,
    MemberSerializer,
    ProjectSerializer,
)


class ApiTestCase(APITestCase):
    def setUp(self):
        self.language_1 = Language.objects.create(id=1, language="Java")
        self.language_2 = Language.objects.create(id=2, language="Python")
        self.specialization = Specialization.objects.create(
            id=1, specialization="Desktop"
        )
        self.member = Member.objects.create(
            id=1,
            first_name="Dima",
            last_name="Rezenkov",
            date_of_birth="2004-03-05",
            summary="From Ukraine",
            email="rezenkovdmitro@gmail.com",
            github_member="https://github.com/RezenkovD",
        )
        self.member.programming_language.add(self.language_1)
        self.member.specialization.add(self.specialization)
        self.project = Project.objects.create(
            title="Dive-into",
            description="Our first project",
            github_project="https://github.com/RezenkovD",
        )
        self.project.specialization.add(self.specialization)
        self.project.programming_language.add(self.language_1)
        self.project.members.add(self.member)

    def test_get_language(self):
        url = reverse("language-list")
        response = self.client.get(url)
        serializer_data = LanguageSerializer(
            [self.language_1, self.language_2], many=True
        ).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_specialization(self):
        url = reverse("specialization-list")
        response = self.client.get(url)
        serializer_data = SpecializationSerializer(
            [self.specialization], many=True
        ).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_member(self):
        url = reverse("member-list")
        response = self.client.get(url)
        serializer_data = MemberSerializer([self.member], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_project(self):
        url = reverse("project-list")
        response = self.client.get(url)
        serializer_data = ProjectSerializer([self.project], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_member_filter(self):
        url = reverse("member-list")
        response = self.client.get(
            url, data={"programming_language": [1], "specialization": [1]}
        )
        serializer_data = MemberSerializer([self.member], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_project_filter(self):
        url = reverse("project-list")
        response = self.client.get(url, data={"members": [1], "specialization": [1]})
        serializer_data = ProjectSerializer([self.project], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_member_search(self):
        url = reverse("member-list")
        response = self.client.get(url, data={"search": "Rezenkov"})
        serializer_data = MemberSerializer([self.member], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_project_search(self):
        url = reverse("project-list")
        response = self.client.get(url, data={"search": "Dive-into"})
        serializer_data = ProjectSerializer([self.project], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
