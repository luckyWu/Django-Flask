# Django-day3

前提：**已经创建好Django项目和名为app的Django应用并且已经配好了数据库**

### 1.对数据库进行增删改查：

* 在Django的app应用中的MODELS中创建3个模型：Student   , Grade ,   Course;

  ```
  class Student(models.Model):
      s_name = models.CharField(max_length=10,null=True,unique=True)
      s_age = models.IntegerField(default=20)
      s_gender = models.BooleanField(default=1)
      class Meta:
          db_table = 'student'
  
  class Grade(models.Model):
      g_name = models.CharField(max_length=10, unique=True)
      class Meta:
          db_table = 'grade'
          
  class Course(models.Model):
      c_name = models.CharField(max_length=10,unique=True)
      class Meta:
          db_table = 'course'
  ```

* 在urls.py文件中

* 1.增加数据：在views.py中建立一个增加数据的视图函数add()

  ```
    from app.models import Student  #导入学生对象
    def add(request):   
    	#增加数据方式1
    	   Student.objects.create(s_name='小红')#增加一行数据：学生姓名为小明，其他字段为默认值
    	#方式2：
          stu = Student()
          stu.s_name = '小明'
          stu.save()
          return HttpResponse('添加成功')
  
    	  
        stu = Student.objects.all()   
        stu = Student.objects.filter(id=1)#和pk=1同效；    
        stu.values('s_name','s_age')#所有对象的字段    
        stu1 = Student.objects.filter(s_name="小红").first()#不存在不会报错；      
        stu = Student.objects.get(s_age=20)#不存在会报错，此方法只能返回一个;    
        stu = Student.objects.filter(s_age=20).filter(s_name="小明")
        stu = Student.objects.filter(yuwen__gt=F('shuxue')+10)#语文比数学大十分      
        stu = Student.objects.filter(s_age=20,s_name="小明")  
        stu = Student.objects.filter(Q(s_age = 18) | Q(s_name = "小明"))  或查询：&  ~
        stu = Student.objects.filter(s_name__contains='1')#模糊查询；    
        stu = Student.objects.filter(s_name__startswith="小")#以小开头；   
        stu = Student.objects.filter(s_name__endswith="1")#以1结尾；  
        stu = Student.objects.filter(s_age__gt=18)#大于     
        stu = Student.objects.filter(s_age__lt=18)#小于   
        stu = Student.objects.order_by('-id') #降序'id'升序  
        stu = Student.objects.exclude(s_age=18)#查询不满足条件的  
        print(len(stu))#stu.count()统计个数
  
  ```

* 删除数据：在views.py中建立一个增加数据的视图函数dele()

  ```
  def dele(request):
  	Student.objects.filter(s_name='小明').delete() #删除小明那一行数据，filter用来筛选数据
  	return HttpResponse('删除成功')
  ```

  





* 修改数据：在views.py中建立一个增加数据的视图函数update()

  ```
  def update(request):
      #方式1：
     #Student.objects.filter(s_name='小明').update(s_name='大明')
      #方式2：
      stu = Student.objects.get(s_name='小红')
      stu.s_name = '大红'
      stu.save()
      return HttpResponse('删除成功')
  ```



* 查找数据：在views.py中建立一个增加数据的视图函数sel():

  ```
  def sel(request):
      Student.objects.all()#获取所有对象;
      stu = Student.objects.filter(id=1) # 获取ID为1的对象和pk=1同效；不存在报错
      stu = Student.objects.get(s_age=20)  # 不存在会报错，此方法只能返回一个对象;
      stu = Student.objects.filter(s_age=20, s_name="小明")#筛选多个条件；
      
      stu = Student.objects.filter(s_name__contains='1')#模糊查询；
      stu = Student.objects.filter(s_name__startswith="小")#以小开头；
      stu = Student.objects.filter(s_name__endswith="1")#以1结尾；
      
      stu = Student.objects.filter(s_age__gt=18)#大于
      stu = Student.objects.filter(s_age__lt=18)#小于
  
      stu = Student.objects.filter(Q(s_age=18) | Q(s_name="小明"))  # 或查询：&(与） ~ （非）需要导入 Q模块
      return HttpResponse('成功')
  ```

* 最后为视图添加URL映射，访问不同的地址实现不同的功能：

  ```
  from app import views
  urlpatterns = [
      url(r'^admin/', admin.site.urls),#django自带的，下面3个是需要添加的；
      url(r'^sel/',views.sel),
      url(r'^dele/',views.dele),
      url(r'^update/',views.update),
  ]
  ```

## 2.建立一对一关系：

1.为学生添加附加信息，在模型中定义:

```
    class StudentInfo(models.Model): 
        phone = models.CharField(max_length=11,null=True)  
        address = models.CharField(max_length=100)  
        stu = models.OneToOneField(Student)  
        class Meta:       
            db_table = 'student_info'
```

​    

2.建立一对一关系：在Student类中添加约束：stu = models.OneToOneField(Student)

```
1.通过学生对象获取学生的附加信息：学生对象.<小写的附加信息类名>
Student.objects.get(s_age=20). studentinfo
2.通过学生的附加信息获取相应学生对象：附加信息相应对象.stu
 StudentInfo.objects.get(phone='15723066479').stu
```



## 2.建立多对多关系

1.在定义Course模型:

```
class Course(models.Model):
    c_name = models.CharField(max_length=10,unique=True)
    class Meta:
        db_table = 'course'
```

2.Course（课程）和Student(学生)是多对多关系：在课程中添加关联语句：

stu = models.ManyToManyField(Student)，之后会自动生成一个course_stu的中间表

```
1.通过学生对象获取课程信息：
Student.objects.get(s_age=20). course_set.all()
2.通过课程信息获取相应学生对象：附加信息相应对象.stu.all()
Course.objects.get(c_name='语文').stu.all()
```



## 3.建立一对多关系：

* 1.在定义Grade模型:

  ```
  class Grade(models.Model):
      g_name = models.CharField(max_length=10, unique=True)
      class Meta:
          db_table = 'grade'
  ```

* 2.在Student中添加关联语句：grade = models.ForeignKey(Grade,null=True)

  

  ```
  1.通过学生对象获取年级信息：
  
  Student.objects.get(s_age=20). grade
  
  2.通过年级信息获取相应学生对象：相应的年级信息.student_set.all()
  
  Course.objects.get(c_name='语文').student_set.all()
  
  ```

  