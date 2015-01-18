# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CropGeoPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('accuracy', models.DecimalField(max_digits=19, decimal_places=6)),
                ('longitude', models.DecimalField(max_digits=19, decimal_places=6)),
                ('latitude', models.DecimalField(max_digits=19, decimal_places=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlantSpacing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('height', models.DecimalField(max_digits=19, decimal_places=2)),
                ('width', models.DecimalField(max_digits=19, decimal_places=2)),
                ('units', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserCrop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crop', models.CharField(max_length=50)),
                ('crop_type', models.CharField(max_length=50)),
                ('variety', models.CharField(max_length=50)),
                ('crop_season', models.CharField(max_length=100)),
                ('acrearage_under_production', models.DecimalField(max_digits=19, decimal_places=2)),
                ('input_cost_per_acre', models.DecimalField(max_digits=19, decimal_places=2)),
                ('annual_production', models.DecimalField(max_digits=19, decimal_places=2)),
                ('market_supplied', models.CharField(max_length=50)),
                ('volume_sold', models.DecimalField(max_digits=19, decimal_places=2)),
                ('volume_lost_in_PH', models.DecimalField(max_digits=19, decimal_places=2)),
                ('value_of_crop_insured', models.DecimalField(max_digits=19, decimal_places=2)),
                ('total_loan_accessed', models.DecimalField(max_digits=19, decimal_places=2)),
                ('user', models.ForeignKey(related_name='crops', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('sub_county', models.CharField(max_length=30)),
                ('parish', models.CharField(max_length=30)),
                ('village', models.CharField(max_length=30)),
                ('user', models.ForeignKey(related_name='locations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.CharField(max_length=13)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(max_length=1, choices=[(b'm', b'male'), (b'f', b'female')])),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='plantspacing',
            name='crop',
            field=models.OneToOneField(related_name='plant_spacing', to='apps.UserCrop'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cropgeopoint',
            name='crop',
            field=models.ForeignKey(related_name='geo_points', to='apps.UserCrop'),
            preserve_default=True,
        ),
    ]
