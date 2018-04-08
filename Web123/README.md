#Instuctions on how to build website through Django
#启动服务器：   python manage.py runserver
#关闭服务器：   ctrl + c

1.allow others in same web use this web
  settings.py
      ALLOWED_HOSTS = ['xxx.xxx.xxx.xxx'] (ipconfig to check your IP)
  python manage.py runserver 0.0.0.0:8000

2.logon admin system
    python manage.py runserver
    http://127.0.0.1:8000/admin

3.create superuser (andywei513)
    python manage.py createsuperuser

4.active models
   (1) settings.py 中，修改INSTALLED_APPS，引入要用到的Application
   (2) 执行终端命令
        python manage.py makemigrations
        python manage.py migrate

   (3) 将model添加到admin.py里
       from .models import Article
       admin.site.register(Article)



5. 配置mysql数据库 settings.py
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '3306',
              }
         }

     默认设置：
     DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                }
             }

6.指定数据库驱动
    django.db.backends.postgresql  # PostgreSQL
    django.db.backends.mysql       # mysql
    django.db.backends.sqlite3     # sqlite
    django.db.backends.oracle      # oracle


7. pymysql使用方法

    pymysql.Connect()参数说明
    host(str):      MySQL服务器地址
    port(int):      MySQL服务器端口号
    user(str):      用户名
    passwd(str):    密码
    db(str):        数据库名称
    charset(str):   连接编码

    connection对象支持的方法
    cursor()        使用该连接创建并返回游标
    commit()        提交当前事务
    rollback()      回滚当前事务
    close()         关闭连接

    cursor对象支持的方法
    execute(op)     执行一个数据库的查询命令
    fetchone()      取得结果集的下一行
    fetchmany(size) 获取结果集的下几行
    fetchall()      获取结果集中的所有行
    rowcount()      返回数据条数或影响行数
    close()         关闭游标对象

8.使用sqlite3
   sqlite3 db.sqlite3
   .quit 退出
