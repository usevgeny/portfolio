# Generated by Django 3.2.6 on 2021-11-28 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myname', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url')),
                ('presentation', models.TextField(blank=True)),
                ('meta_desc', models.CharField(blank=True, max_length=160)),
                ('meta_keys', models.CharField(blank=True, max_length=300)),
                ('my_photo', models.ImageField(blank=True, upload_to='photos/<django.db.models.fields.CharField>', verbose_name='Img')),
            ],
            options={
                'ordering': ['-myname'],
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url')),
                ('meta_desc', models.CharField(blank=True, max_length=160)),
                ('meta_keys', models.CharField(blank=True, max_length=300)),
                ('is_published', models.BooleanField(default=True, verbose_name='Published')),
            ],
            options={
                'ordering': ['-years'],
            },
        ),
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url')),
                ('icon', models.CharField(max_length=1000)),
            ],
            options={
                'ordering': ['interest'],
            },
        ),
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url')),
                ('intro', models.TextField(blank=True)),
                ('meta_desc', models.CharField(blank=True, max_length=160)),
                ('meta_keys', models.CharField(blank=True, max_length=300)),
                ('my_photo', models.ImageField(blank=True, upload_to='photos/<django.db.models.fields.CharField>', verbose_name='Img')),
            ],
            options={
                'ordering': ['-intro_name'],
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url')),
                ('lang_percent', models.IntegerField(default=0, verbose_name='lang_percent')),
            ],
            options={
                'ordering': ['lang_percent'],
            },
        ),
        migrations.CreateModel(
            name='PrivateSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('destination_chat', models.CharField(max_length=15)),
                ('bot_id', models.CharField(max_length=46)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url')),
                ('description', models.TextField(blank=True)),
                ('meta_desc', models.CharField(blank=True, max_length=160)),
                ('meta_keys', models.CharField(blank=True, max_length=300)),
                ('photo', models.ImageField(blank=True, upload_to='photos/<django.db.models.fields.CharField>', verbose_name='Img')),
                ('is_published', models.BooleanField(default=True, verbose_name='Published')),
            ],
            options={
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url')),
                ('skill_percent', models.IntegerField(default=0, verbose_name='lang_percent')),
            ],
            options={
                'ordering': ['skill_percent'],
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url')),
                ('work_description', models.TextField(blank=True)),
                ('meta_desc', models.CharField(blank=True, max_length=160)),
                ('meta_keys', models.CharField(blank=True, max_length=300)),
                ('work_photo', models.ImageField(blank=True, upload_to='photos/<django.db.models.fields.CharField>', verbose_name='Img')),
                ('is_published', models.BooleanField(default=True, verbose_name='Published')),
            ],
            options={
                'ordering': ['-work_title'],
            },
        ),
    ]
