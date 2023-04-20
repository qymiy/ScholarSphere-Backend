from django.db import models



class User(models.Model):
    # 基础信息
    # username = models.CharField('用户名', max_length=100, default='')
    password = models.CharField('密码', max_length=32)
    email = models.EmailField()
    # times_of_wa_password、
    times_of_wa_password = models.IntegerField('一天内密码输错次数',default=0)
    # forbiden_start_time、
    forbiden_start_time = models.DateTimeField('禁止登陆开始时间',default=None)
    # 7days_autologin_start_time
    sevendays_autologin_start_time = models.DateTimeField('设置自动登录开始时间',default=None)




