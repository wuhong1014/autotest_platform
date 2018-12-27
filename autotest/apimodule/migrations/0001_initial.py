# Generated by Django 2.1.3 on 2018-12-04 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modulename', models.CharField(max_length=64, unique=True, verbose_name='模块名称')),
                ('moduledesc', models.CharField(max_length=200, verbose_name='模块描述')),
                ('moduler', models.CharField(max_length=200, verbose_name='模块负责人')),
                ('isexec', models.BooleanField(verbose_name='是否执行')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '模块管理',
                'verbose_name_plural': '模块管理',
                'db_table': 'api_module',
            },
        ),
    ]
