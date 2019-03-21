import os
import time

import celery
from django.test import TestCase

# Create your tests here.
import random
from io import StringIO
import requests
from django_redis import get_redis_connection

# 注册环境变量（注册Django配置文件）
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'duanxin.settings')
# 创建Celery的实例 - broker代表消息代理（从哪里获取消息队列服务）
app = celery.Celery('app.tests',broker='redis://127.0.0.1:6379/5')
# 读取Django项目的配置信息
app.config_from_object('django.conf:settings')


def gen_mobile_code(length=6):
    """生成指定长度的手机验证码"""
    code = StringIO()
    for _ in range(length):
        code.write(str(random.randint(0, 9)))
    return code.getvalue()

@app.task
def send_by_luosimao(tel, code):
    """发送短信验证码（调用螺丝帽短信网关）"""
    print('--------------------0001111110000---------------------')
    resp = requests.post(
        # url='http://sms-api.luosimao.com/v1/send.json',
        url = 'https://sms-api.luosimao.com/v1/status.json',
        auth=('api', '1c8653b1cce7dcda40ad691b387a348c'),
        data={
            'mobile': tel,
            'message': f'您的验证码为{code}。【铁壳测试】'
        },
        timeout=10,
        verify=False)
    # Django框架封装好的缓存调用方式
    # caches['default'].set(f'mobile_code:{tel}', code, timeout=120)
    # 通过django_redis的函数获得原生的Redis连接进行操作（比较强大）
    print('--------------------00003333333330---------------------')
    cli = get_redis_connection(alias='default')
    cli.set(tel, code, ex=120)
    print('--------------------000000000000000---------------------')
    # time.sleep(10)
    return resp.content



# request.session['mobile_code'] = code
# 如果调用短信网关的函数返回字典对象就用JsonResponse进行处理
# 如果返回的是字符串就用HttpResponse并指定MIME类型即可
# 调用三方平台的一个风险就是时间不可预估 但是我们的应用不能够因为三方平台而阻塞
# 所以通常调用三方平台而且不需要马上获得执行结果的场景都要进行异步化的处理
# 让发送短信的函数延迟执行（将函数调用变成一条消息放到消息队列）- 消息的生产者
# send_sms_by_luosimao.delay(tel, code)
@app.task
def add(x, y):
    time.sleep(10.0)
    return x+y