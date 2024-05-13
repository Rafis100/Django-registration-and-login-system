# Generated by Django 4.1.2 on 2024-05-12 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_project_projectfile_delete_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectfile',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_files', to='users.project'),
        ),
    ]
