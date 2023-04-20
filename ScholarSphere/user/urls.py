
from django.urls import path
from .views import *

urlpatterns = [
    path('user/register', register),
    path('user/checkmailregistered',checkmailregistered )
    # 这是一个样例，指定路由名为url_name，对应处理函数为当前app内views.py中的api_name
]