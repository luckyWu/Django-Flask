#django中HttpRequest请求
**视图的第一个参数必须是HttpRequest对象**

* ```
  #定义一个视图函数，参数request则是返回的HttpRequest对象（参数可自己起名）
  def login(request):
  	pass
  ```

###在视图函数中，接收的request有如下属性：

* 1.path：一个字符串，表示请求的页面的完整路径，不包含域名。

  ```
  请求的路径，这里的路径是指相对路径，也就是说一个登陆后台页面的请求：
  http://127.0.0.1:8000/admin 的路径是 /admin
  ```

  

* 2.method：一个字符串，表示请求使用的HTTP方法，常用值包括：'GET'、'POST'

    ```
       def login(request):  
    	if request.method == "GET":    #在浏览器中给出地址发出请求采用get方式，如超链接。
      	print('GET成功')       
          return 
      if request.method == "POST":
      #在浏览器中点击表单的提交按钮发起请求，如果表单的method设置为post则为post请求。
      	print('POST成功')       
          return 
    ```

* 3.encoding：一个字符串，表示提交的数据的编码方式。

  ```
      如果为None则表示使用浏览器的默认设置，一般为utf-8。
      这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码，接下来对属性的任何访问将使用新的encoding值。
  
  ```

* 4.GET：一个类似于字典的对象，包含get请求方式的所有参数。

  ```
  例如前端请求url为：http://127.0.0.1:8000/admin/?page=5
  可通过获取get函数获取参数数据：request.GET.get('page')
  ```

  

* POST：一个类似于字典的对象，包含post请求方式的所有参数。

    ```
    常见表单提交数据：request.POST["username"]#若username不存在报错
                    request.POST.get("username"）#若username不存在返回空值
    ```

    

* FILES：一个类似于字典的对象，包含所有的上传文件。

    ```
    # 表单中enctype 属性规定在发送到服务器之前应该如何对表单数据进行编码，默认地，表单数据会编码为 "application/x-www-form-urlencoded"。就是说，在发送到服务器之前，所有字符都会进行编码（空格转换为 "+" 加号，特殊符号转换为 ASCII HEX 值）
    
    # multipart/form-data：不对字符编码。在使用包含文件上传控件的表单时，必须使用该值。
    <form action="" method="POST" enctype='multipart/form-data'>
        文件:<input type="file" name="file"/>
        <input type="submit" name="submit"/>
    </form>
    ```

* COOKIES：一个标准的Python字典，包含所有的cookie，键和值都为字符串。

    ```
     通过COOKIES，可以获取前端发送的cookies信息
     如：request.COOKIES.get('token')
    ```

    

* session：一个既可读又可写的类似于字典的对象，表示当前的会话，只有当Django 启用会话的支持时才可用，详细内容见"状态保持"。

    

* body:请求的主体，返回的是一个`字符串` 