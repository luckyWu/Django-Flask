# Django-day4(模板)

**使用模板，通过Django 的模板可以构建完整的 HTML 页面**

* 1.在 Django 项目配置目录中创建一个名为 templates 的目录。

  ​           注意，这个目录要与项目的 manage.py 脚本放在同一级

  ​          ![ ](img/2.png)

* 2.为templates指定路径，在settings.py中配置;

  ```
  在  TEMPLATES 中添加 'DIRS': [os.path.join(BASE_DIR,'templates')] 指定路径
  BASE_DIR：为当前工程目录路径，通过join方法将BASE_DIR 变量和 'templates' 字符串拼接起来
   
  ```

* 3.在urls.py中的 urlpatterns 列表添加url(r'^app/', include('free.urls')),
     **上面的映射把以 rango/ 开头的 URL 交给 rango 应用处理**

     在app应用下添加urls.py文件,

  ```
  from django.conf.urls import url
  from rango import views
  urlpatterns = [
  url(r'^$', views.index, name='index'),
  ]
  这段代码先导入 Django 处理 URL 映射的函数和 Rango 应用的 views 模块，然后在 urlpatterns
  列表中调用 url 函数映射 index 视图
  ```

* 4.在app应用下的views.py 中定义index的视图函数

  ```
  def index(request):
      return render(request,'index.html')#渲染index页面
  ```

* 5.在templates目录下新建一个index.html文件和base.html文件

* 6.使用base.html作为父模板：打开base.html文件在其中加入两个区块

  ```
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Title</title>
      {% block head %}
      {%  endblock %}
  {% Comment %}
  #这是注释的方法
  Django 模板标签放在 {% 和 %} 之间。因此，区块以 {% block <NAME> %} 开头，其中
  <NAME> 是区块的名称。区块必须以 endblock 结尾，而且也要放在 {% 和 %} 之间，即 {% endblock
  {% endcomment %} 。
  </head>
  <body>
  
     {% block body%}
      {%  endblock %}
  </body>
  </html>
  ```

* 6在index.html中继承父模板并添加内容：

  ```
  {%  extens 'base.html' %}
  
  {% block body%}
     <p>你好</p>   #相当在<body>中写入这句话
  {%  endblock %}
  ```