# flask

1.**最小应用**

```
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
	return 'hello'
if __name__ == '__main__':
	app.run()	#app.run(host, port ,debug=True/False) 
#默认端口5000，host:127.0.0.1
#启动应用：python app.py runserver

```

**2.修改启动方式**

```
#1.安装flask-script使用Manager启动
from flask-script import Manager
from flask import Flask
app = Flask(__name__)
manage = Manager(app)
if __name__ == '__main__':
	manage.run()	
#这样就可以在终端指定主机的ip和端口
# python app.py runserver -h ip -p port -d

```

**3.使用蓝图**

```

```

