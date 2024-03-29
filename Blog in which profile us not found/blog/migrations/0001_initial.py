# Generated by Django 2.2.1 on 2019-06-26 07:22

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
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_logo', models.FileField(blank=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('edited_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
        migrations.CreateModel(
            name='Blogs1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_content', models.CharField(max_length=250)),
                ('is_favorite', models.BooleanField(default=False)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blogs')),
            ],
        ),
    ]
