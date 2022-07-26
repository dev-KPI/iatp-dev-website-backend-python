# Generated by Django 4.0.6 on 2022-08-06 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='programming_language',
            field=models.ManyToManyField(to='api.language'),
        ),
    ]
