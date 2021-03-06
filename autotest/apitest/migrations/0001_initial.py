# Generated by Django 2.1.3 on 2018-12-04 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apimodule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apino', models.CharField(max_length=100, unique=True, verbose_name='用例编号')),
                ('apiname', models.CharField(max_length=100, verbose_name='接口名称')),
                ('apiurl', models.CharField(max_length=100, verbose_name='url地址')),
                ('apimethod', models.CharField(choices=[('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'), ('patch', 'patch')], default='get', max_length=200, null=True, verbose_name='请求方法')),
                ('apiheaders', models.CharField(max_length=200, verbose_name='headers')),
                ('apiparamvalue', models.CharField(max_length=1000, null=True, verbose_name='请求参数和值')),
                ('apiresult', models.CharField(max_length=200, verbose_name='预期结果')),
                ('apiexec', models.BooleanField(verbose_name='是否执行')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('apimodule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apimodule.Module', verbose_name='功能模块')),
            ],
            options={
                'verbose_name': '单一场景接口',
                'verbose_name_plural': '单一场景接口',
                'db_table': 'single_api_test',
            },
        ),
        migrations.CreateModel(
            name='Apitest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apitestid', models.CharField(max_length=20, unique=True, verbose_name='流程用例ID')),
                ('apitestname', models.CharField(max_length=256, verbose_name='流程用例名称')),
                ('apitestdesc', models.CharField(max_length=512, verbose_name='流程用例描述')),
                ('apitestparamsvalue', models.CharField(max_length=1000, null=True, verbose_name='参数')),
                ('apitester', models.CharField(max_length=16, verbose_name='测试负责人')),
                ('apitestresult', models.CharField(max_length=20, verbose_name='预期结果')),
                ('apitestexec', models.BooleanField(verbose_name='是否执行')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('apitestmodule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apimodule.Module', verbose_name='功能模块')),
            ],
            options={
                'verbose_name': '流程场景接口',
                'verbose_name_plural': '流程场景接口',
                'db_table': 'api_test',
            },
        ),
    ]
