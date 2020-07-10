# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-13 09:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import pcontact.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.TextField(max_length=200)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Company',
            },
        ),
        migrations.CreateModel(
            name='CompanyAssociation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('year', models.CharField(blank=True, max_length=30, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pcontact.Company')),
            ],
            options={
                'verbose_name_plural': 'Company Association',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('role', multiselectfield.db.fields.MultiSelectField(choices=[('Angel', 'Angel'), ('Expert', 'Expert'), ('GP', 'GP'), ('LP', 'LP')], max_length=100)),
                ('past_investment', models.CharField(blank=True, max_length=100, null=True)),
                ('img_file', models.ImageField(blank=True, null=True, upload_to=pcontact.models.get_image_path)),
                ('img_url', models.URLField(blank=True, null=True)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('company', models.ManyToManyField(to='pcontact.CompanyAssociation')),
                ('connection', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_name', models.TextField(max_length=200)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Institute',
            },
        ),
        migrations.CreateModel(
            name='InsttitueAssociation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(blank=True, max_length=30, null=True)),
                ('degree', models.CharField(default='', max_length=200)),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pcontact.Institute')),
            ],
            options={
                'verbose_name_plural': 'Institute Association',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='contacts',
            name='institute',
            field=models.ManyToManyField(to='pcontact.InsttitueAssociation'),
        ),
        migrations.AddField(
            model_name='contacts',
            name='tags',
            field=models.ManyToManyField(blank=True, to='pcontact.Tags'),
        ),
    ]
