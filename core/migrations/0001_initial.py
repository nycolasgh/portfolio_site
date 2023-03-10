# Generated by Django 4.0.5 on 2022-10-01 18:29

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
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.TextField(null=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='about')),
            ],
            options={
                'verbose_name': 'About me',
                'verbose_name_plural': 'About me',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientname', models.CharField(blank=True, max_length=100, null=True, verbose_name='Client name')),
                ('companyname', models.CharField(max_length=100, null=True, verbose_name='Company name')),
                ('description', models.TextField(verbose_name='Company Description')),
                ('image', models.ImageField(default='default.png', upload_to='clients')),
                ('clientuser', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Service name')),
                ('description', models.TextField(null=True, verbose_name='About Service')),
            ],
        ),
        migrations.CreateModel(
            name='RecentWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Work title')),
                ('description', models.CharField(max_length=400, verbose_name='Work Description')),
                ('image', models.ImageField(upload_to='works')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(blank=True, related_name='Services', to='core.service')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.client')),
            ],
        ),
        migrations.CreateModel(
            name='Feedbacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientname', models.CharField(max_length=100, null=True, verbose_name='Username')),
                ('companyname', models.CharField(max_length=100, null=True, verbose_name='Company name')),
                ('feedback', models.TextField(verbose_name='Feedback')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
