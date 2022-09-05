from django.test import TestCase
from api.models import Language, Specialization, Member, Project
from api.serializers import (
    LanguageSerializer,
    SpecializationSerializer,
    MemberSerializer,
    ProjectSerializer,
)


class SpecializationSerializerTestCase(TestCase):
    def test_ok_specialization(self):
        specialization_1 = Specialization.objects.create(id=1, specialization="Desktop")
        data = SpecializationSerializer(specialization_1).data
        expected_data = [{"id": 1, "specialization": "Desktop"}]
        self.assertEqual(expected_data[0], data)


class LanguageSerializerTestCase(TestCase):
    def test_ok_language(self):
        language_1 = Language.objects.create(id=1, language="Java")
        data = LanguageSerializer(language_1).data
        expected_data = [{"id": 1, "language": "Java"}]
        self.assertEqual(expected_data[0], data)


class ProjectSerializerTestCase(TestCase):
    def test_ok_project(self):
        project_1 = Project.objects.create(
            title="Dive-into",
            description="Our first project",
            github_project="https://github.com/RezenkovD",
        )
        language = Language.objects.create(id=1, language="Java")
        specialization = Specialization.objects.create(id=1, specialization="Android")
        member = Member.objects.create(
            id=1,
            first_name="Dima",
            last_name="Rezenkov",
            date_of_birth="2004-03-05",
            summary="From Ukraine",
            email="rezenkovdmitro@gmail.com",
            github_member="https://github.com/RezenkovD",
        )
        project_1.programming_language.add(language)
        project_1.specialization.add(specialization)
        project_1.members.add(member)
        data = ProjectSerializer(project_1).data
        expected_data = [
            {
                "id": 1,
                "title": "Dive-into",
                "description": "Our first project",
                "github_project": "https://github.com/RezenkovD",
                "members": [1],
                "specialization": [1],
                "programming_language": [1],
            }
        ]
        self.assertEqual(expected_data[0], data)


class MemberSerializerTestCase(TestCase):
    def test_ok_member(self):
        language = Language.objects.create(id=1, language="JS")
        specialization = Specialization.objects.create(id=1, specialization="WEB")
        member_1 = Member.objects.create(
            first_name="Dima",
            last_name="Rezenkov",
            date_of_birth="2004-03-05",
            summary="From Ukraine",
            email="rezenkovdmitro@gmail.com",
            github_member="https://github.com/RezenkovD",
        )
        member_1.programming_language.add(language)
        member_1.specialization.add(specialization)
        data = MemberSerializer(member_1).data
        expected_data = [
            {
                "id": 1,
                "first_name": "Dima",
                "last_name": "Rezenkov",
                "date_of_birth": "2004-03-05",
                "summary": "From Ukraine",
                "email": "rezenkovdmitro@gmail.com",
                "github_member": "https://github.com/RezenkovD",
                "programming_language": [1],
                "specialization": [1],
            }
        ]
        self.assertEqual(expected_data[0], data)
