from django.test import TestCase
from api.models import Language, Specialization, Member, Project, SocialLinks, GitHubLinks
from api.serializers import (
    LanguageSerializer,
    SpecializationSerializer,
    MemberCreateSerializer,
    ProjectCreateSerializer,
    SocialLinksSerializer,
    GitHubLinksSerializer,
)


class SpecializationSerializerTestCase(TestCase):
    def test_ok_specialization(self):
        specialization = Specialization.objects.create(id=1, specialization="Desktop")
        data = SpecializationSerializer(specialization).data
        expected_data = [{"id": 1, "specialization": "Desktop"}]
        self.assertEqual(expected_data[0], data)


class LanguageSerializerTestCase(TestCase):
    def test_ok_language(self):
        language = Language.objects.create(id=1, language="Java")
        data = LanguageSerializer(language).data
        expected_data = [{"id": 1, "language": "Java"}]
        self.assertEqual(expected_data[0], data)


class ProjectSerializerTestCase(TestCase):
    def test_ok_project(self):
        project = Project.objects.create(
            id=1,
            photo_url="http://127.0.0.1:8000/docs#/",
            title="Dive-into",
            description="Our first project",
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
        )
        project.programming_language.add(language)
        project.specialization.add(specialization)
        project.members.add(member)
        data = ProjectCreateSerializer(project).data
        expected_data = [
            {
                "id": 1,
                "photo_url": "http://127.0.0.1:8000/docs#/",
                "title": "Dive-into",
                "description": "Our first project",
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
        member = Member.objects.create(
            photo_url="https://drive.google.com/file/d/1KzK3R5CktEDWbexP2FsbyIn28R4qsbdF/view?usp=sharing",
            first_name="Dima",
            last_name="Rezenkov",
            date_of_birth="2004-03-05",
            summary="From Ukraine",
            email="rezenkovdmitro@gmail.com",
        )
        member.programming_language.add(language)
        member.specialization.add(specialization)
        data = MemberCreateSerializer(member).data
        expected_data = [
            {
                "id": 1,
                "photo_url": "https://drive.google.com/file/d/1KzK3R5CktEDWbexP2FsbyIn28R4qsbdF/view?usp=sharing",
                "first_name": "Dima",
                "last_name": "Rezenkov",
                "date_of_birth": "2004-03-05",
                "summary": "From Ukraine",
                "email": "rezenkovdmitro@gmail.com",
                "programming_language": [1],
                "specialization": [1],
            }
        ]
        self.assertEqual(expected_data[0], data)


class SocialLinksSerializersTestCase(TestCase):
    def test_ok_sociallinks(self):
        language = Language.objects.create(id=1, language="JS")
        specialization = Specialization.objects.create(id=1, specialization="WEB")
        member = Member.objects.create(
            id=1,
            first_name="Dima",
            last_name="Rezenkov",
            date_of_birth="2004-03-05",
            summary="From Ukraine",
            email="rezenkovdmitro@gmail.com",
        )
        member.programming_language.add(language)
        member.specialization.add(specialization)
        link = SocialLinks.objects.create(
            id=1, social_link="GH", link="https://github.com", member=member
        )
        data = SocialLinksSerializer(link).data
        expected_data = [
            {
                "id": 1,
                "social_link": "GH",
                "link": "https://github.com",
                "member": 1,
            }
        ]
        self.assertEqual(expected_data[0], data)


class GitHubLinksSerializerTestCase(TestCase):
    def test_ok_githublinks(self):
        project = Project.objects.create(
            photo_url="http://127.0.0.1:8000/docs#/",
            title="Dive-into",
            description="Our first project",
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
        )
        project.programming_language.add(language)
        project.specialization.add(specialization)
        project.members.add(member)
        githublink = GitHubLinks.objects.create(
            id=1, title="Backend", link="https://github.com", project=project
        )
        data = GitHubLinksSerializer(githublink).data
        expected_data = [
            {
                "id": 1,
                "title": "Backend",
                "link": "https://github.com",
                "project": 1,
            }
        ]
        self.assertEqual(expected_data[0], data)
