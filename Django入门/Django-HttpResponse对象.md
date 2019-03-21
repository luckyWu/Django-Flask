# Django-HttpResponse对象

```
视图在接收请求并处理后，必须返回HttpResponse对象或子对象。
在django.http模块中定义了HttpResponse对象的API。
HttpRequest对象由Django创建，HttpResponse对象由开发人员创建。 
```

**关于HttpResponse的构造函数**

* HttpResponse.__init__(content='', content_type=None, status=200, reason=None, charset=None) 

* #### 属性

  - content：表示返回的内容，字符串类型
  - charset：表示response采用的编码字符集，字符串类型
  - status_code：响应的HTTP响应状态码
  - content-type：指定输出的MIME类型

  ```
  def index(request):
          return HttpResponse('相应成功！！')#响应成功后前端页面将会显示<'相应成功！！'>
          # 后面几个参数一般不需要指定
          #content_type：默认主体类型为text/html，使用 DEFAULT_CHARSET 的值来指定文件编码，默认             为：'utf-8'
          #charset：如果没有给定（也就是为None），将会从 content_type 中提取，如果提取不成功， 那么           DEFAULT_CHARSET 的设定将被使用。  
  ```

 ### HttpResponseRedirect  

* HttpResponseRedirect 属于HttpResponse的子类，实现重定向，服务器端跳转

```
def index(request):
        res = HttpResponseRedirect('http://127.0.0.1:8080/all_stu/')#直接写重定向的地址
        res = HttpResponseRedirect(reverse('app:index'))#通过反向解析获取地址
        # 反向解析需导入模块：from django.urls import reverse
        # app为URL的命名空间在工程目录下的URLS.py中设置:
        #如：url(r'^app/',include('app.urls',namespace='app'))；
        # index是视图Url的别名，在应用的Urls.py（没有就新建一个）中设置   
        # 如：url(r'^index/',views.index,name='aindex'),
        return res
```

* set_cookie （）方法---cookie的设置 

  Cookie是由服务器端生成，发送给User-Agent（一般是浏览器），浏览器会将Cookie的key/value保存到某个目录下的文本文件内，下次请求同一网站时就发送该Cookie给服务器（前提是浏览器设置为启用cookie） 

  ```
  set_cookie参数：set_cookie(key, value='', max_age=None, expires=None, path='/', domain=None, secure=None, httponly=False)  
  ###下面只讨论前四个参数；
      key：键名，字符串形式。
  　　value：对应的值，字符串形式。
  　　max_age：cookie 过期的相对时间，单位是秒。如果为None，则当浏览器关闭的时候过期。如果设置了 max_age 而没有设置 expires，则 expires 将根据 max_age 的值计算出来。
  　　expires：设置 cookie 过期的绝对时间。应该是一个 UTC（Universal Time Coordinated） "Wdy, DD-Mon-YY HH:MM:SS GMT" 格式的字符串
  　　
  　　 如：res.set_cookie('token', token, max_age=6000)#6000秒后失效
  ```

  

  

### render() 函数-渲染模板

**render方法可接收三个参数，一是request参数，二是待渲染的html模板文件,三是保存具体数据的字典参数。**

**它的作用就是将数据填充进模板文件，最后把结果返回给浏览器**

```
def test(request):
    msg = 'good'
    return render(request, 'test.html',{'msg':msg})#第三个参数可不写，写了将返回给前端这个字典
```

