# Generated by Django 2.2.1 on 2019-06-08 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='blog_content',
        ),
        migrations.CreateModel(
            name='blogs1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_content', models.CharField(max_length=250)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blogs')),
            ],
        ),
    ]