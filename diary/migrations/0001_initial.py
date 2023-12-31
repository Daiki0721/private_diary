# Generated by Django 4.2.7 on 2023-11-22 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Title')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Content')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Picture1')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Picture2')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Picture3')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Upload date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update dates')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Diary',
            },
        ),
    ]
