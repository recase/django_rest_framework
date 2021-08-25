# Generated by Django 3.2.5 on 2021-07-30 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('excerpt', models.TextField(null=True)),
                ('post', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_on', models.DateTimeField(blank=True, default=None, null=True)),
                ('status', models.CharField(choices=[('published', 'published'), ('draft', 'draft')], default='published', max_length=20)),
                ('slug', models.SlugField(max_length=100, unique_for_date='created_at')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]