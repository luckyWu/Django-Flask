# Django-day2

新建一个django工程，用pycharm 打开

* 1.创建一个名称为APP的应用，在Terminal中执行：python.manage.py startapp app;

    执行后工程目录下会增加一个app文件夹

   ![](img/1.png)

  

* 2. 在项目的 urls.py 文件中添加一个映射，指向新建的应用：

     *  先导入 Django 处理 URL 映射的函数和 app应用的 views 模块，然后在 urlpatterns

     ​        列表中调用 url 函数映射 hello视图 

     ```
     from django.conf.urls import url #导入 Django 处理 URL 映射的函数模块
     from app import views  # app应用的 views 模块
     urlpatterns = [
         url(r'^hello/',views.hello)#调用 url 函数映射 hello视图 
         ]
     ```

     ​                

* 3.在app文件中创建一个名为hello的视图
  * （1）：从 django.http 模块中导入 HttpResponse 对象；
  * （2）：创建一个名为hello的视图函数；
  * （3）：视图函数至少有一个参数，即一个 HttpRequest 对象，它也在 django.http 模块中。按约
    定，这个参数名为 request；
  * （4）：必须返回一个 HttpResponse 对象

```
      from django.http import HttpResponse
      def hello(request):
      return HttpResponse('html')
```
* 4.创建数据模型（已经配置好数据库）在app文件models.py添加：

```
class Student(models.Model):
    s_name = models.CharField(max_length=6,unique=True)#定义s_name字段，varchar 类型，最长不超过6个字符，唯一；
    s_age= models.IntegerField(default=18)
    s_gender = models.BooleanField(default=1)

    class Meta:
        db_table = 'student'#定义模型迁移到数据库中的表名；
        
```
* 5. 把应用名称添加到项目配置目录中的 settings.py 文件里

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',#-------------------------------->添加的app名称
]
```

* 6.在Terminal中执行python.manage.py makemigrations：

​                生成迁移文件

* 7.在Terminal中执行python.manage.py migrate

​                将模型迁移到数据库





# 模型的CRUD

* 1.创建：模型名.objects.create(name=xxx,age=xxx)

* 2.查询：

  * 查询所有：模型名.objects.all()

  * 查询满足条件：

    * 模型名.objects.filter(条件1).filter(条件2)

    *  模型名.objects.filter(条件1，条件2)

    * 查询第一个、最后一个：first()、last()

    * 获取确定的某一个：    模型名.objects.get(条件) ;(注意：条件不满足报错，返回对象只能                               是一个)

    * 排除满足条件：模型名.objects.exclude(条件)

    * 返回结果序列化：模型名.objects.values(name=xxx,age=xxx);

    * 排序:模型名.objects.order_by('id/-id')

    * 查询过滤条件：__ contains（包含）,   __ startwith （以..开始）, __ gt (大于),   __ lt(小于) ,  __ gte

      

      

      

      

      

    ​                                             



![1540262813496](C:\Users\ADMINI~1\AppData\Local\Temp\1540262813496.png)    











