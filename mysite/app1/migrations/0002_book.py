# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('about', models.CharField(max_length=500)),
                ('library', models.ForeignKey(to='app1.Library')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
