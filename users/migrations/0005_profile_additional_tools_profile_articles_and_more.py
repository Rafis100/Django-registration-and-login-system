# Generated by Django 4.1.2 on 2024-05-06 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='additional_tools',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='articles',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='count_subscribers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='count_subscriptions',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='experience',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='foreign_language',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='hackathons',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='hard_skills',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_visible_repository',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_pictures/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='programming_languages',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='projects',
            field=models.FileField(blank=True, upload_to='profile_projects/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='soft_skills',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='telephone',
            field=models.IntegerField(blank=True, max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(max_length=500),
        ),
    ]
