## FengWeb
Lns-XueFeng的个人网站

## Web开发流程
#### 前端开发流程

- 根据功能规格书画页面草图
- 根据草图做交互式原型图
- 根据原型图开发前端页面

#### 后端开发流程

- 数据库建模
- 编写表单类
- 编写视图函数和相关处理函数
- 在页面中使用jinja2替换虚拟数据

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
         --- css
         --- images
         --- musics
         --- markdown
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