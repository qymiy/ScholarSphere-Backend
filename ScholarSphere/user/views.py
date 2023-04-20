# publish/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from  user.models import User

def check_number(password):
    for c in password:
        if c.isnumeric():
            return True


def check_letter(password):
    for c in password:
        if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
            return True


def check_mark(password):
    for c in password:
        if not (c.isnumeric() or 'a' <= c <= 'z' or 'A' <= c <= 'Z'):
            return True
def check_legal(password):
    if len(password) < 8 or len(password) > 16:
        return {'result': 0, 'message': '长度需为8-16个字符,请重新输入。'}
    else:
        for i in password:
            if 0x4e00 <= ord(i) <= 0x9fa5 or ord(i) == 0x20:  # Ox4e00等十六进制数分别为中文字符和空格的Unicode编码
                return {'result': 0, 'message': '不能使用空格、中文，请重新输入。'}
        else:
            key = 0
            key += 1 if check_number(password) else 0
            key += 1 if check_letter(password) else 0
            key += 1 if check_mark(password) else 0
            if key >= 2:
                return {'result': 1, 'message': '密码强度合适'}
            else:
                return {'result': 0, 'message': '至少含数字/字母/字符2种组合，请重新输入。'}

def check_password(email,password):
    if User.objects.filter(email=email, password=password).exists():
        return True
    return False

def check_password_wrong_45times(email):
    user = User.objects.filter(email=email)
    if(user.times_of_wa_password==5):
        user.times_of_wa_password=0
        return True
    user.times_of_wa_password=user.times_of_wa_password+1
    user.save()
    return False


@csrf_exempt    # 跨域设置
def register(request):
    """
    :param request: 请求体
    :return:        1 - 成功， 0 - 失败
    请求体包含包含 username，password1，password2，email
    """
    if request.method == 'POST':

        # username = request.POST.get('username', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        email = request.POST.get('email', '')

        if  len(password1) == 0 or len(password2) == 0 or len(email) == 0:
            result = {'result': 0, 'message': r'用户名, 邮箱, 与密码不允许为空!'}
            return JsonResponse(result)

        if User.objects.filter(email=email).exists():
            result = {'result': 0, 'message': r'该邮箱已被注册'}
            return JsonResponse(result)

        if password1 != password2:
            result = {'result': 0, 'message': r'两次密码不一致!'}
            return JsonResponse(result)

        message = check_legal(password1)

        user = User( email=email, password=password1)
        user.save()
        result = {'result': 1, 'message': r"注册成功!"}
        return JsonResponse(result)
    else:
        result = {'result': 0, 'message': r"请求方式错误！"}
        return JsonResponse(result)

@csrf_exempt
def checkmailregistered(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            result = {'result': 0, 'message': r'该邮箱已被注册!'}
            return JsonResponse(result)
        result = {'result': 1, 'message': r"新邮箱,可以注册!"}
        return result
    else:
        result = {'result': 0, 'message': r"请求方式错误！"}
        return JsonResponse(result)