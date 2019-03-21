import datetime
from django.utils import timezone
from uuid import uuid1
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from user.models import User, UserToken
from user.tests import my_md5_hex


def login(request):
    if request.method == "GET":
        return render(request, 'index.html')
    if request.method == "POST":
        status = {'code':100, 'message':'登陆成功'}
        username = request.POST['username']
        password = request.POST['password']
        password = my_md5_hex(password)
        user = User.objects.filter(username=username, password=password).first()
        if user:
            status['userid'] = request.session['userid'] = user.id
            with transaction.atomic():
                status['token'] = token = uuid1().hex
                UserToken.objects.update_or_create(user=user, defaults={'token': token})
                current_time = timezone.now()
                if user.lastlogin:
                    delta = current_time - user.lastlogin
                    if delta.days >= 1:
                        user.point += 5
                        user.lastlogin = current_time
                        user.save()
                else:
                    user.lastlogin = current_time
                    user.save()
        else:
            status['code'] = '30001'
            status['message'] = '用户名或密码错误'
        return JsonResponse(status)


def test(request):
    print(request.session["userid"])
    return render(request,"test.html")


def userToken(request):
    """token验证"""
    id = request.session['userid']
    accept_token = request.META.get("HTTP_AUTHORIZATION")
    token=UserToken.objects.filter(user=1).first().token
    if token == 1:#accept_token:
        return JsonResponse({"msg":"恭喜无需登陆直接进入"})
    return JsonResponse({"msg":"请登陆！！！"})