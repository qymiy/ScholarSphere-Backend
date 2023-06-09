# Generated by Django 4.2 on 2023-04-22 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='forbiden_start_time',
            field=models.DateTimeField(default=None, null=True, verbose_name='禁止登陆开始时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sevendays_autologin_start_time',
            field=models.DateTimeField(default=None, null=True, verbose_name='设置自动登录开始时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='times_of_wa_password',
            field=models.IntegerField(default=0, null=True, verbose_name='一天内密码输错次数'),
        ),
    ]
