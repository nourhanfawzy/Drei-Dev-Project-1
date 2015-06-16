# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book_name', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='library',
            name='created_by',
            field=models.ForeignKey(related_name='library', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notification',
            name='library',
            field=models.ForeignKey(to='app1.Library'),
        ),
        migrations.AddField(
            model_name='notification',
            name='notified_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
