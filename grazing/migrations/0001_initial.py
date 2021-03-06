# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allotment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allotment_number', models.CharField(max_length=11)),
                ('allotment_unique', models.CharField(max_length=255)),
                ('allotment_name', models.CharField(max_length=255)),
                ('available_for_grazing', models.CharField(max_length=1)),
                ('grazing_decision', models.CharField(max_length=255)),
                ('public_acres', models.FloatField()),
                ('amp_text', models.CharField(max_length=255)),
                ('amp_implement_date', models.DateTimeField(null=True)),
                ('management_stat_text', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Authorization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=55)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Boundary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allotment_name', models.CharField(max_length=255, null=True)),
                ('allotment_number', models.CharField(max_length=55, null=True)),
                ('allotment_unique', models.CharField(max_length=255, null=True)),
                ('state', models.CharField(max_length=2, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('allotment', models.ForeignKey(to='grazing.Allotment', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FieldOffice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('office_code', models.CharField(max_length=55)),
                ('office_name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allotment_name', models.CharField(max_length=255, null=True)),
                ('allotment_unique', models.CharField(max_length=55, null=True)),
                ('land_health_eval_date', models.DateTimeField(null=True, blank=True)),
                ('causal_factors_date', models.DateTimeField(null=True, blank=True)),
                ('land_health_status', models.NullBooleanField()),
                ('livestock_factor', models.NullBooleanField()),
                ('description', models.TextField(null=True)),
                ('nepa_date', models.DateTimeField(null=True, blank=True)),
                ('nepa_identifier', models.CharField(max_length=55)),
                ('permit_status', models.CharField(max_length=55)),
                ('year_released', models.IntegerField(null=True)),
                ('allotment', models.ForeignKey(to='grazing.Allotment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NEPAType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('abbr', models.CharField(max_length=4, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('operator_display_name', models.CharField(max_length=255)),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('st2', models.CharField(max_length=255)),
                ('zipcode15', models.CharField(max_length=255)),
                ('zipcode69', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('release_text', models.CharField(max_length=255)),
                ('auth_no', models.ManyToManyField(to='grazing.Authorization')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Permit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pl_effect_dt', models.DateTimeField()),
                ('pl_exp_dt', models.DateTimeField()),
                ('permit_status', models.CharField(max_length=50)),
                ('livestock_number', models.FloatField()),
                ('livestock_kind', models.CharField(max_length=25)),
                ('pd_beg_dt', models.DateTimeField()),
                ('pd_end_dt', models.DateTimeField()),
                ('type_use', models.CharField(max_length=50)),
                ('pl_percent', models.FloatField()),
                ('aums', models.FloatField()),
                ('allotment', models.ForeignKey(to='grazing.Allotment')),
                ('auth_no', models.ForeignKey(to='grazing.Operator')),
                ('field_office', models.ForeignKey(to='grazing.FieldOffice')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('abbr', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='health',
            name='auth_no',
            field=models.ForeignKey(to='grazing.Operator'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='health',
            name='field_office',
            field=models.ForeignKey(to='grazing.FieldOffice'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='health',
            name='nepa_type',
            field=models.ForeignKey(to='grazing.NEPAType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fieldoffice',
            name='state',
            field=models.ForeignKey(to='grazing.State'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='allotment',
            name='auth_no',
            field=models.ManyToManyField(to='grazing.Operator', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='allotment',
            name='field_office',
            field=models.ForeignKey(to='grazing.FieldOffice'),
            preserve_default=True,
        ),
    ]
