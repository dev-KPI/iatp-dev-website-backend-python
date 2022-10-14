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
    photo_url = models.URLField(max_length=256, null=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    date_of_birth = models.DateField(blank=True)
    summary = models.TextField(max_length=1024, help_text="Enter your summary")
    programming_language = models.ManyToManyField(Language)
    specialization = models.ManyToManyField(Specialization)
    email = models.EmailField(max_length=256)

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


class SocialLinks(models.Model):
    GITHUB = "GH"
    GITLAB = "GL"
    TELEGRAM = "TG"
    LINKENID = "LD"
    DISCORD = "DS"
    SOCIAL_LINK_CHOICES = [
        (GITHUB, "Github"),
        (GITLAB, "Gitlab"),
        (TELEGRAM, "Telegram"),
        (LINKENID, "Linkenid"),
        (DISCORD, "Discord"),
    ]
    social_link = models.CharField(
        max_length=2, choices=SOCIAL_LINK_CHOICES, default=GITHUB
    )
    link = models.URLField(max_length=256)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.social_link
