## FengWeb
Lns-XueFeng的个人网站

## 开发流程
- 数据库建模
- 编写表单类
- 编写视图函数和相关处理函数
- 在页面中使用jinja2替换虚拟数据

## 网站外观
<img src="./index.png">


## 功能安排
<img src="./function.jpg">

## 项目目录
```
fengweb
     blueprints
         --- __init__.py
         --- blog.py
         --- admin.py
         --- auth.py
     static
         --- js
         --- css
         --- images
         --- musics
         --- markdown
         --- ckeditor
     templates
         --- blog
         --- auth
         --- admin
         --- error
         --- base.html
     __init__.py
     commands.py
     extensions.py
     forms.py
     models.py
     settings.py
     utils.py 
```