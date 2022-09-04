from django.db import models


# Create your models here.


class Specialization(models.Model):
    specialization = models.CharField(max_length=32)

    def __str__(self):
        return self.specialization


class Language(models.Model):
    language = models.CharField(max_length=32)

    def __str__(self):
        return self.language


class Member(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    date_of_birth = models.DateField(blank=True)
    summary = models.TextField(max_length=1024, help_text="Enter your summary")
    programming_language = models.ManyToManyField(Language)
    specialization = models.ManyToManyField(Specialization)
    email = models.EmailField(max_length=256)
    github_member = models.URLField(max_length=200)

    def __str__(self):
        return "{0} {1}".format(self.last_name, self.first_name)


class Project(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(
        max_length=1000, help_text="Enter project description"
    )
    members = models.ManyToManyField(Member)
    github_project = models.URLField(max_length=256)
    specialization = models.ManyToManyField(Specialization)
    programming_language = models.ManyToManyField(Language)

    def __str__(self):
        return self.title
