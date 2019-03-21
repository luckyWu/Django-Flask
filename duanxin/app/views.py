import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django_redis import get_redis_connection

from app.capt import gen_captcha_text, Captcha
from app.tests import gen_mobile_code, send_by_luosimao, add


def register(request):
    """注册页面"""
    if request.method == "GET":
        print('GET成功')
        return render(request, 'register.html')
    if request.method == "POST":
        tel = request.POST.get('tel')
        code = request.POST.get('code')
        input_capt = request.POST.get('capt')
        cli = get_redis_connection(alias='default')
        capt_code = request.session['captcha_code']
        code_redis = (cli.get(tel)).decode('utf-8')
        if code_redis==code and input_capt==capt_code:
            return HttpResponse('OK')
        return HttpResponse('false')


def send(request):
    """发送短信验证码"""
    if request.method == "POST":
        tel = request.POST.get('mobile')
        print(tel,type(tel))
        code = gen_mobile_code()
        s=send_by_luosimao.delay(tel, code)
        # print(s)
        # res = json.loads(s.decode('utf-8'))
        return JsonResponse({'code': 20000, 'message': '短信验证码已经发出'})

def res(request):
    add.delay(1, 2)
    return JsonResponse({'code': 20000, 'message': '短信验证码已经发出'})


def graph(request):
    """获取图片验证码"""
    code_text = gen_captcha_text()
    request.session['captcha_code'] = code_text
    code_bytes = Captcha.instance().generate(code_text)
    return HttpResponse(code_bytes, content_type='image/png')