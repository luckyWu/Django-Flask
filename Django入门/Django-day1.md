# Django-day1



Django====>MVT模型

M(模型)

V(视图):处理业务逻辑；

T(模板Template):页面；

**1.python2 需要配置环境变量，pytho3则不用**

**2.virtualenv**（创建一套独立的python运行环境)

> 先在电脑中创建一个文件夹，然后在文件夹中再创建两个文件夹：一个文件夹是虚拟环境的目录，一个文件夹用来放创建的工程；

1.pip install virtualenv #安装虚拟环境软件

2.virtualenv --no-site-package -p 路径 <虚拟环境名称> #创建虚拟环境

 （路径 ： 指定安装在虚拟机中的python版本，不指定者为环境变量中的 ）

3.激活虚拟环境：进入虚拟目录下>Script下通过执行activate激活虚拟环境；（使用deactivate退出虚拟环境；）

4.在虚拟环境Script目录下使用PIP装软件；

5.pip install django==1.11 #安装jango1.11  (与python3.7版本冲突)

* pip list :查询当前site-package装了多少库;
* pip freeze:查看所有安装过的包 

6.进入工作文件夹执行   django-admin startproject <项目名>  #创建工程



**3.打开pycharm 导入建好的工程**

![1540201308649](img/1540201308649.png)

（会自动生成5个文件，manage.py:工具集管理入口；__ init __.py; settings.py;urls.py;wsgi.py;

* 1.在Terminal 中输入python.manage.py runserver 8000  （运行本地服务器,django自动提供一个后台）

* 2.改语言---------在settings.py中 改 LANGUAGE_CODE = 'en-us'#''en-us'代表英文 ，‘ zh-hans'代表中文

* 3.(让别人访问自己的服务器）在Terminal 中输入python.manage.py runserver 0.0.0.0：8000运行本地服务器

* 4.![1540194640470](img/1540194640470.png)

  * 通过编辑配置使其点击DEbug 直接就能启动django

  

* 5. 连接MYSQL数据库：

     1.在settings.py中修改DATABASES 中的信息（例如下表）

     ```
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',#指明使用什么数据库，这里用MYSQL
             'NAME': 'dj6',      #数据库的名称
             'USER':'root',      #数据库的用户名 
             'PASSWORD':'123456',# 密码
             'HOST':'127.0.0.1',  #目标地址
             'PORT':3306           #端口号
         }
     ```

     2.Python2用MySQLdb 驱动连接；

     3.python3 需要操作pip install  pymysql ，并在__ init __.py文件中添加

   * import pymysql  
   * pymysql.install_as_MySQLdb()

* 6. 使用python manage.py migrate迁移（Django自带的模型映射到数据库）
      * ![1540200424589](img/1540200424589.png)
      * 数据库中会出现10张表。

* 7. 在Terminal中使用python manage.py createsuperuser 创建超级管理员用户名和密码；

      













