# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('agent', models.CharField(verbose_name='客户端名称', max_length=64)),
                ('score', models.IntegerField(verbose_name='客户端分数')),
            ],
            options={
                'verbose_name_plural': '用户分数表',
                'db_table': 'userrank',
            },
        ),
    ]
