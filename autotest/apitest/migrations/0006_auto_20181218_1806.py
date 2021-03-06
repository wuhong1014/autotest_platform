# Generated by Django 2.1.3 on 2018-12-18 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0005_auto_20181218_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apis',
            name='apifunc',
            field=models.CharField(max_length=20, verbose_name='函数'),
        ),
        migrations.AlterField(
            model_name='apis',
            name='apiheaders',
            field=models.CharField(max_length=200, verbose_name='headers'),
        ),
        migrations.AlterField(
            model_name='apis',
            name='apimethod',
            field=models.CharField(choices=[('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'), ('patch', 'patch')], default='get', max_length=200, verbose_name='请求方法'),
        ),
        migrations.AlterField(
            model_name='apis',
            name='apiparamvalue',
            field=models.CharField(max_length=1000, verbose_name='请求参数和值'),
        ),
        migrations.AlterField(
            model_name='apitest',
            name='apitestparamsvalue',
            field=models.CharField(max_length=1000, verbose_name='参数'),
        ),
    ]
