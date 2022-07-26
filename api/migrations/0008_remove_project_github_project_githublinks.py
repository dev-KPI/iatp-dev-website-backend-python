# Generated by Django 4.0.6 on 2022-10-19 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_project_photo_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='github_project',
        ),
        migrations.CreateModel(
            name='GitHubLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('link', models.URLField(max_length=256)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='github_links', to='api.project')),
            ],
        ),
    ]
