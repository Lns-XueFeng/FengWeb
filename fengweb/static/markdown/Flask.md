## Flask

此笔记整理自Flask Web开发的相关书籍，理清知识脉络以及方便自己时常查阅。

### Flask简介

#### 介绍

在大多数标准中，Flask都算是小型框架，小到可以称为“微框架”。Flask非常小，因此你一旦能够熟练使用它，很可能就能读懂它所有的源码（真的吗？我不信滑稽😂）。

Flask有3个主要依赖：路由、调试和Web服务器网关接口（WSGI，Web server gateway interface）子系统由Werkzeug提供；模板系统由Jinja2提供；命令行集成由Click提供。

Flask原生不支持数据库访问、Web表单验证和用户身份验证等高级功能。这些功能以及其他大多数Web应用需要的核心服务都以扩展的形式实现，然后再与核心包集成。

#### 虚拟环境

创建虚拟环境 -> 使用虚拟环境 -> 激活虚拟环境 -> pip安装Flask -> 激活虚拟环境 -> 使用flask run命令启动Web开发服务器

在Python 3中，虚拟环境由Python标准库中的venv包原生支持。创建虚拟环境的命令格式如下：

```shell
$ python3 -m venv virtual-environment-name
```

-m venv选项的作用是以独立的脚本运行标准库中的venv包，后面的参数为虚拟环境的名称。

下面我们在flasky目录中创建一个虚拟环境。通常，虚拟环境的名称为venv，不过你也可以使用其他名称。确保当前目录是flasky，然后执行这个命令：

```shell
$ python3 -m venv venv
```

这个命令执行完毕后，flasky目录中会出现一个名为venv的子目录，这里就是一个全新的虚拟环境，包含这个项目专用的Python解释器。

若想使用虚拟环境，要先将其“激活”。如果你使用的是Linux或macOS，可以通过下面的命令激活虚拟环境：

```shell
$ source venv/bin/activate
```

若想使用虚拟环境，要先将其“激活”。如果你使用的是Windows，可以通过下面的命令激活虚拟环境：

```shell
# 注意提前切换到相应目录
$ .\venv\Scripts\activate.bat   # 在CMD下
$ .\venv\Scripts\activate.ps1   # 在PowerShell下
```

虚拟环境被激活后，里面的Python解释器的路径会添加到当前命令会话的PATH环境变量中，指明在什么位置寻找一众可执行文件。为了提醒你已经激活了虚拟环境，激活虚拟环境的命令会修改命令提示符，加入环境名。

激活虚拟环境后，在命令提示符中输入python，将调用虚拟环境中的解释器，而不是系统全局解释器。如果你打开了多个命令提示符窗口，在每个窗口中都要激活虚拟环境。

虚拟环境中的工作结束后，在命令提示符中输入deactivate，还原当前终端会话的PATH环境变量，把命令提示符重置为最初的状态。

Python包使用包管理器pip安装，所有虚拟环境中都有这个工具。与python命令类似，在命令提示符会话中输入pip将调用当前激活的虚拟环境中的pip工具。

```shell
(venv) $ pip install flask
```

执行这个命令后，pip不仅安装Flask自身，还会安装它的所有依赖。任何时候都可以使用pip freeze命令查看虚拟环境中安装了哪些包：

```shell
(venv) $ pip freeze
click==6.7
Flask==0.12.2
itsdangerous==0.24
Jinja2==2.9.6
MarkupSafe==1.0
Werkzeug==0.12.2
```

### Flask入门

#### 创建应用

所有Flask应用都必须创建一个应用实例。Web服务器使用一种名为Web服务器网关接口的协议（WSGI），把接收自客户端的所有请求都转交给这个对象处理。应用实例是Flask类的对象，通常由下述代码创建：

```python
from flask import Flask

app = Flask(__name__)   # __name__参数必须指定
```

Flask用这个参数（_\_name__）确定应用的位置，进而找到应用中其他文件的位置，例如图像和模板。还有更复杂的初始化方式，目前仅使用此方式即可。

#### 视图函数

客户端（例如Web浏览器）把请求发送给Web服务器，Web服务器再把请求发送给Flask应用实例。应用实例需要知道对每个URL的请求要运行哪些代码，所以保存了一个URL到Python函数的映射关系。处理URL和函数之间关系的程序称为路由。

```python
# 定义一个路由
@app.route('/')   # 前提是理解Python装饰器
def index():
    return "<h1>Hello World</h1>"
```

前例把index()函数注册为应用根地址的处理程序。使用app.route装饰器注册视图函数是首选方法，但不是唯一的方法。Flask还支持一种更传统的方式：使用app.add_url_rule()方法。这个方法最简单的形式接受3个参数：URL、端点名和视图函数。下述示例使用app.add_url_rule()方法注册index()函数，其作用与前例相同：

```python
# 另外一种方式
def index():
    return "<h1>Hello World</h1>"

app.add_url_rule('/', "index", index)
```

以上两种方式创建的函数即为视图函数，其中的路径为相对路径，假如我们的服务器域名为：www.codechangeworld.cn，则index的绝对路径为：www.codechangeworld.cn/，如果已部署应用，当浏览器发起www.codechangeworld.cn/这个路径的请求时，index视图函数会被激活进行处理返回响应。

此外，app.route()还支持可变的url，如下：

```python
# 动态路由
@app.route("/user/<name>")
def user(name):
    return f"<h1>Hello {name}"

"""
路由中的动态部分默认使用字符串，不过也可以是其他类型。例如，路由/user/<int:id>只会匹配动态片段id为整数的URL，例如/user/123。Flask支持在路由中使用string、int、float和path类型。path类型是一种特殊的字符串，与string类型不同的是，它可以包含正斜线。
"""
```

路由URL中放在尖括号里的内容就是动态部分，任何能匹配静态部分的URL都会映射到这个路由上。调用视图函数时，Flask会将动态部分作为参数传入函数。在这个视图函数中，name参数用于生成个性化的欢迎消息。

```python
# 一个完整的flask应用
from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def index(name):
    return f"Helllo {name}"
```

#### 开发服务器

Flask应用自带Web开发服务器（用于开发与测试），通过flask run命令启动。这个命令在FLASK_APP环境变量指定的Python脚本中寻找应用实例。

若想启动前面编写的hello.py应用，首先确保之前创建的虚拟环境已经激活，而且里面安装了Flask。Windows用户执行下述命令启动Web服务器：

```shell
(venv) $ set FLASK_APP=hello.py
(venv) $ flask run
* Serving Flask app "hello"
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Linux和macOS用户和Windows用户仅设置环境变量的命令不同，Linux和macOS用户为export命令，其他均一致。

启动Web开发服务器之后即可在浏览器输入http://localhost:5000/访问服务器。而如果在基URL输入了别的内容，因为应用并没有定义相应的视图函数，因此会返回404错误码，表示没有此页面。

```python
# 另外一种启动Web服务器的方式
if __name__ == "__main__":
    app.run()
```

#### 调试模式

Flask应用可以在调试模式中运行。在这个模式下，开发服务器默认会加载两个便利的工具：重载器和调试器。

启用重载器后，Flask会监视项目中的所有源码文件，发现变动时自动重启服务器。在开发过程中运行启动重载器的服务器特别方便，因为每次修改并保存源码文件后，服务器都会自动重启，让改动生效。

调试器是一个基于Web的工具，当应用抛出未处理的异常时，它会出现在浏览器中。此时，Web浏览器变成一个交互式栈跟踪，你可以在里面审查源码，在调用栈的任何位置计算表达式。

调试模式默认禁用。若想启用，在执行flask run命令之前设定FLASK_DEBUG=1环境变量：

```shell
(venv) $ set FLASK_APP=hello.py
(venv) $ set FLASK_DEBUG=1
(venv) $ flask run
* Serving Flask app "hello"
* Forcing debug mode on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active
* Debugger PIN: 273-181-528
```

使用app.run()方法启动服务器时，不会用到FLASK_APP和FLASK_DEBUG环境变量。若想以编程的方式启动调试模式，就使用app.run(debug=True)。

千万不要在生产服务器中启用调试模式。客户端通过调试器能请求执行远程代码，因此可能导致生产服务器遭到攻击。作为一种简单的保护措施，启动调试模式时可以要求输入PIN码，执行flask run命令时会打印在控制台中。

#### 命令行选项

**1.Flask自带命令：**

flask命令支持一些选项。执行flask --help，或者执行flask而不提供任何参数，可以查看哪些选项可用：

```shell
Usage: flask [OPTIONS] COMMAND [ARGS]...

  A general utility script for Flask applications.

  An application to load must be given with the '--app' option, 'FLASK_APP'
  environment variable, or with a 'wsgi.py' or 'app.py' file in the current
  directory.

Options:
  -e, --env-file FILE   Load environment variables from this file. python-
                        dotenv must be installed.
  -A, --app IMPORT      The Flask application or factory function to load, in
                        the form 'module:name'. Module can be a dotted import
                        or file path. Name is not required if it is 'app',
                        'application', 'create_app', or 'make_app', and can be
                        'name(args)' to pass arguments.
  --debug / --no-debug  Set debug mode.
  --version             Show the Flask version.
  --help                Show this message and exit.

Commands:
  routes  Show the routes for the app.
  run     Run a development server.
  shell   Run a shell in the app context.
```

flask shell命令在应用的上下文中打开一个Python shell会话。在这个会话中可以运行维护任务或测试，也可以调试问题。

--host参数特别有用，它告诉Web服务器在哪个网络接口上监听客户端发来的连接。默认情况下，Flask的Web开发服务器监听localhost上的连接，因此服务器只接受运行服务器的计算机发送的连接。下述命令让Web服务器监听公共网络接口上的连接，因此同一网络中（同一局域网）的其他计算机发送的连接也能接收到：

```python
(venv) $ flask run --host 0.0.0.0
* Serving Flask app "hello"
* Running on http//0.0.0.0:5000/ (Press CTRL+C to quit)
```

现在，网络中的任何计算机都能通过http://a.b.c.d:5000访问Web服务器。其中，a.b.c.d是运行服务器的计算机的IP地址。

--reload、--no-reload、--debugger和--no-debugger参数对调试模式进行细致的设置。例如，启动调试模式后可以使用--no-debugger关闭调试器，但是应用还在调试模式中运行，而且重载器也启用了。

**2.用户自定义命令：**

通过创建任意一个函数，并为其添加app.cli.command()装饰器，我们就可以注册一个Flask命令。还可以利用click这个库给咱们的命令添加选项之类的，关于更多的自定义命令设置和功能去查阅click的说明文档：

```python
@app.cli.command()
def say_hello():
    click.echo("Hello World")
```

#### 项目配置

在很多情况下，你需要设置程序的某些行为，这时你就需要使用配置变量。在Flask中，配置变量就是一些大写形式的Python变量，你也可以称之为配置参数或配置键。使用统一的配置变量可以避免在程序中以硬编码的形式设置程序。

在一个项目中，你会用到许多配置，Flask提供的配置，扩展提供的配置，还有程序特定的配置。和平时使用变量不同，这些配置变量都通过Flask对象的app.config属性作为统一的接口来设置和获取，它指向的Config类实际上是字典的子类，所以你可以像操作其他字典一样操作它。

Flask提供了很多种方式来加载配置：

**1.类似操作字典那样：**

```python
app.config["ADMIN_NAME"] = "xuefeng"
# 或者这样
app.config.update(
	TESTING=True,
    SECRET_KEY = "_dapwifjafi"
)
```

**2.将配置变量单独存储在Python脚本中：**

```python
# 假设有一个config.py
app.config.from_pyfile("config.py")
```

**3.将配置变量单独存储在JSON文件内：**

```python
# 假设有一个JSON文件config.json
app.config.from_file("config.json", load=json.load)
```

**4.将配置变量放在Python的类中：**

```
# 假设有一个Python类Config
app.config.from_object(Config)
```

### 请求与响应

#### 应用与请求上下文

Flask从客户端收到请求时，要让视图函数能访问一些对象，这样才能处理请求。请求对象就是一个很好的例子，它封装了客户端发送的HTTP请求。

为了避免大量可有可无的参数把视图函数弄得一团糟，Flask使用上下文临时把某些对象变为全局可访问。有了上下文，便可以像下面这样编写视图函数：

```python
from flask import request

@app.route('/')
def index():
    user_agent = request.headers.get("User-Agent")
    return f"<p>Your browser is {user_agent}<p>"
```

注意，在这个视图函数中我们把request当作全局变量使用。事实上，request不可能是全局变量。试想，在多线程服务器中，多个线程同时处理不同客户端发送的不同请求时，每个线程看到的request对象必然不同。Flask使用上下文让特定的变量在一个线程中全局可访问，与此同时却不会干扰其他线程。

**Flask上下文**

在Flask中有两种上下文：应用上下文和请求上下文。表2-1列出了这两种上下文提供的变量。

| 变量名      | 上下文     | 说明                                                   |
| ----------- | ---------- | ------------------------------------------------------ |
| current_app | 应用上下文 | 当前应用的应用实例                                     |
| g           | 应用上下文 | 处理请求时用作临时存储的对象，每次请求都会重设这个变量 |
| request     | 请求上下文 | 请求对象，封装了客户端发出的HTTP请求中的内容           |
| session     | 请求上下文 | 用户会话，值为一个字典，存储请求之间需要记住的值       |

Flask在分派请求之前激活（或推送）应用和请求上下文，请求处理完成后再将其删除。应用上下文被推送后，就可以在当前线程中使用current_app和g变量。类似地，请求上下文被推送后，就可以使用request和session变量。如果使用这些变量时没有激活应用上下文或请求上下文，就会导致错误。

下述Python shell会话演示了应用上下文的使用方法：

```python
>>> from hello import app
>>> from flask import current_app
>>> current_app.name
Traceback (most recent call last)
...
RuntimeError: working outside of application context
>>> app_ctx = app.app_context()
>>> app_ctx.push()
>>> current_app.name
"hello"
>>> app_ctx.pop()
```

在这个例子中，没激活应用上下文之前就调用current_app.name会导致错误，但推送完上下文之后就可以调用了。注意，获取应用上下文的方法是在应用实例上调用app.app_context()。

#### 请求分派

应用收到客户端发来的请求时，要找到处理该请求的视图函数。为了完成这个任务，Flask会在应用的URL映射中查找请求的URL。URL映射是URL和视图函数之间的对应关系。Flask使用app.route装饰器或者作用相同的app.add_url_rule()方法构建映射。可通过app.url_map查看当前app实例应用的URL映射情况。

URL映射中的(HEAD, OPTIONS, GET)是请求方法，由路由进行处理。HTTP规范中规定，每个请求都有对应的处理方法，这通常表示客户端想让服务器执行什么样的操作。Flask为每个路由都指定了请求方法，这样即使不同的请求方法发送到相同的URL上时，也会使用不同的视图函数处理。

#### 请求对象

Flask通过上下文变量request对外开放请求对象。这个对象非常有用，包含客户端发送的HTTP请求的全部信息。Flask请求对象中最常用的属性和方法见下表：

| 属性或方法   | 说明                                                         |
| ------------ | ------------------------------------------------------------ |
| form         | 一个字典，存储请求提交的所有表单字段                         |
| args         | 一个字典，存储通过URL查询字符串传递的所有参数                |
| values       | 一个字典，form和args的合集                                   |
| cookies      | 一个字典，存储请求的所有cookie                               |
| headers      | 一个字典，存储请求所有的HTTP首部                             |
| files        | 一个字典，存储请求上传的所有文件                             |
| get_data()   | 返回请求主体缓冲的数据                                       |
| get_json()   | 返回一个Python字典，包含解析请求主体后得到的JSON             |
| blueprint    | 处理请求的Flask蓝本的名称                                    |
| endpoint     | 处理请求的Flask端点的名称；Flask把视图函数的名称用作路由端点的名称 |
| method       | HTTP请求方法，例如GET或POST                                  |
| scheme       | URL方案（http或https）                                       |
| is_secure()  | 通过安全的连接（HTTPS）发送请求时返回True                    |
| host         | 请求定义的主机名，如果客户端定义了端口号，还包括端口号       |
| path         | URL的路径部分                                                |
| query_string | URL的查询字符串部分，返回原始二进制值                        |
| full_path    | URL的路径和查询字符串部分                                    |
| url          | 客户端请求的完整URL                                          |
| base_url     | 同url，但是没有查询字符串部分                                |
| remote_addr  | 客户端的IP地址                                               |
| environ      | 请求的原始WSGI环境字典                                       |

#### 请求钩子

有时在处理请求之前或之后执行代码会很有用。例如，在请求开始时，我们可能需要创建数据库连接或者验证发起请求的用户身份。为了避免在每个视图函数中都重复编写代码，Flask提供了注册通用函数的功能，注册的函数可在请求被分派到视图函数之前或之后调用。请求钩子通过装饰器实现。Flask支持以下四种钩子：

| 钩子                    | 说明                                                         |
| ----------------------- | ------------------------------------------------------------ |
| @before_request()       | 注册一个函数，在每次请求之前运行                             |
| @before_first_request() | 注册一个函数，只在处理第一个请求之前运行，可以通过这个钩子添加服务器初始化任务 |
| @after_request()        | 注册一个函数，如果没有未处理的异常抛出，在每次请求之后运行   |
| @teardown_request()     | 注册一个函数，即使有未处理的异常抛出，也在每次请求之后运行   |
| @after_this_request     | 在视图函数内注册一个函数，会在这个请求结束后运行             |

在请求钩子函数和视图函数之间共享数据一般使用上下文全局变量g。例如，before_request处理程序可以从数据库中加载已登录用户，并将其保存到g.user中。随后调用视图函数时，便可以通过g.user获取用户。

#### 响应对象

Flask调用视图函数后，会将其返回值作为响应的内容。多数情况下，响应就是一个简单的字符串，作为HTML页面回送客户端。

但HTTP协议需要的不仅是作为请求响应的字符串。HTTP响应中一个很重要的部分是状态码，Flask默认设为200，表明请求已被成功处理。

如果视图函数返回的响应需要使用不同的状态码，可以把数字代码作为第二个返回值，添加到响应文本之后。例如，下述视图函数返回400状态码，表示请求无效：

```python
@app.route('/')
def index():
    return "Bad Request", 400
```

视图函数返回的响应还可接受第三个参数，这是一个由HTTP响应首部组成的字典。

如果不想返回由1个、2个或3个值组成的元组，Flask视图函数还可以返回一个响应对象。make_response()函数可接受1个、2个或3个参数（和视图函数的返回值一样），然后返回一个等效的响应对象。有时我们需要在视图函数中生成响应对象，然后在响应对象上调用各个方法，进一步设置响应。下例创建一个响应对象，然后设置cookie：

```python
from flaks import make_response

@app.route('/')
def index():
    response = make_response("<h1>This is a document carries a cookies</h1>")
    response.set_cookie("answer", "42")
```

响应对象最常使用的属性和方法见下表：

| 属性或方法      | 说明                                         |
| --------------- | -------------------------------------------- |
| status_code     | HTTP数字状态码                               |
| headers         | 一个类似字典的对象，包含随响应发送的所有首部 |
| set_cookie()    | 为响应添加一个cookie                         |
| delete_cookie() | 删除一个cookie                               |
| content_length  | 响应主体的长度                               |
| content_type    | 响应主体的媒体类型                           |
| set_data()      | 使用字符串或字节值设定响应                   |
| get_data()      | 获取响应主体                                 |

响应有个特殊的类型，称为重定向。这种响应没有页面文档，只会告诉浏览器一个新URL，用以加载新页面。

重定向的状态码通常是302，在Location首部中提供目标URL。重定向响应可以使用3个值形式的返回值生成，也可在响应对象中设定。不过，由于使用频繁，Flask提供了redirect()辅助函数，用于生成这种响应：

```python
from flask import redirect

@app.route('/')
def index():
    return redirect("http://www.example.com")
```

还有一种特殊的响应由abort()函数生成，用于处理错误。在下面这个例子中，如果URL中动态参数id对应的用户不存在，就返回状态码404：

```python
from flask import abort

@app.route("/user/<id>")
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return f"<h1>Hello, {user}"
```

注意，abort()不会把控制权交还给调用它的函数，而是抛出异常。

| Status Code | Explanation                       |
| :---------- | :-------------------------------- |
| 200         | 请求成功                          |
| 301         | 资源（网页等）被永久转移到其它URL |
| 404         | 请求的资源（网页等）不存在        |
| 500         | 内部服务器错误                    |

#### Cookie与Session

HTTP是无状态协议。也就是说，再一次请求响应结束之后，服务器不会留下任何关于对方状态的信息。但是对于某些Web程序来说，需要记住某些信息以提供某些服务，而解决这个问题的便是Cookie技术。

Cookie技术通过在请求和响应报文中添加Cookie数据来保存客户端的状态信息。

```python
@app.route("/set/<name>")
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie("name", name)
    return response
```

**set_cookie()方法的参数：**

| 属性     | 说明                                                     |
| -------- | -------------------------------------------------------- |
| key      | cookie的键                                               |
| value    | cookie的值                                               |
| max_age  | cookie被保存的时间数，单位为秒，默认在用户会话结束时过期 |
| expires  | 具体的过期时间，一个datetime对象或者UNIX时间戳           |
| path     | 限制cookie只在给定的路径可用，默认为整个域名             |
| domain   | 设置cookie可用的域名                                     |
| secure   | 如果设为True，只有通过HTTPS才可以使用                    |
| httponly | 如果设为True，禁止客户端JavaScript获取cookie             |

**Session：安全的Cookie**

Flask提供了session对象用来将Cookie数据加密储存。

**设置程序密钥：**

```python
app.secret_key = "this is a secret string"
```

更安全的做法是将密钥写进系统环境变量，或者是保存在.env文件中（这个文件别上传到Github）：

```txt
# 假装这是.env文件
SECRET_KEY="secret string"
```

```python
import os 
# ...
app.secret_key = os.getenv("SECRET_KEY", "secret_key")
```

**模拟用户认证：**

```python
from flask import redirect, url_for

@app.route("/login")
def login():
	...
    if login_right:
        ...
        session["logged_in"] = True
        flash("You are login success")
        return redirect(url_for('index'))
     flash("Sorry Error, Please login again")
     return redirect(url_for(login)

@app.route("/logout")
def logout():
    session["logged_in"] = Flase
    flash("You are logout success")
    return redirect(url_for("index"))
```

通过session还可以实现更多与用户的交互，比如记录用户看视频的进度，用户上次选择的主题等等。

#### Flask扩展

Flask的设计考虑了可扩展性，故而没有提供一些重要的功能，例如数据库和用户身份验证，所以开发者可以自由选择最适合应用的包，或者按需求自行开发。

社区成员开发了大量不同用途的Flask扩展，如果这还不能满足需求，任何Python标准包或代码库都可以使用。

关于响应，还有一个很重要的部分没有介绍，下面来进行介绍。

### 模板Template

把业务逻辑和表现逻辑混在一起会导致代码难以理解和维护。假设要为一个大型表格构建HTML代码，表格中的数据由数据库中读取的数据以及必要的HTML字符串连接在一起。把表现逻辑移到模板中能提升应用的可维护性。

模板是包含响应文本的文件，其中包含用占位变量表示的动态部分，其具体值只在请求的上下文中才能知道。使用真实值替换变量，再返回最终得到的响应字符串，这一过程称为渲染。为了渲染模板，Flask使用一个名为Jinja2的强大模板引擎。

#### 模板与Jinja2

**1.定义与渲染**

形式最简单的Jinja2模板就是一个包含响应文本的文件。看如何定义与渲染：

```jinja2
// templates/index.html
<h1>Hello {{ name }} </h1>
```

默认情况下，Flask在应用目录中的templates子目录里寻找模板。

```python
from flask import Flask, render_template

# ...

@app.route('/<name>')
def index(name):
    return render_template("index.html", name=name)
```

Flask提供的render_template()函数把Jinja2模板引擎集成到了应用中。这个函数的第一个参数是模板的文件名，随后的参数都是键–值对，表示模板中变量对应的具体值。在这段代码中，第二个模板收到一个名为name的变量。

前例中的name=name是经常使用的关键字参数，如果你不熟悉的话，可能不知所云。左边的name表示参数名，就是模板中使用的占位符；右边的name是当前作用域中的变量，表示同名参数的值。两侧使用相同的变量名是很常见，但不是强制要求。

**2.变量**

前面在模板中使用的{{ name }}结构表示一个变量，这是一种特殊的占位符，告诉模板引擎这个位置的值从渲染模板时使用的数据中获取。

Jinja2能识别所有类型的变量，甚至是一些复杂的类型，例如列表、字典和对象。下面是在模板中使用变量的一些示例：

```jinja2
<p>A value from a dictionary: {{ mydict['key'] }}.</p>
<p>A value from a list: {{ mylist[3] }}.</p>
<p>A value from a list, with a variable index: {{ mylist[myintvar] }}.</p>
<p>A value from an object's method: {{ myobj.somemethod() }}.</p>
```

变量的值可以使用过滤器修改。过滤器添加在变量名之后，二者之间以竖线分隔。

下面列出了Jinja2提供的部分**常用过滤器：**

| 过滤器名   | 说明                                       |
| ---------- | ------------------------------------------ |
| safe       | 渲染值时不转义                             |
| capitalize | 把值的首字母转换成大写，其他字母转换成小写 |
| lower      | 把值转化成小写形式                         |
| upper      | 把值转换成大写形式                         |
| title      | 把值中每个单词的首字母都转换成大写         |
| trim       | 把值的首尾空格删掉                         |
| striptags  | 渲染之前把值中所有的HTML标签都删掉         |

safe过滤器值得特别说明一下。默认情况下，出于安全考虑，Jinja2会转义所有变量。例如，如果一个变量的值为'\<h1>Hello\</h1>'，Jinja2会将其渲染成'&lt;h1&gt;Hello&lt;/ h1&gt;'，浏览器能显示这个h1元素，但不会解释它。很多情况下需要显示变量中存储的HTML代码，这时就可使用safe过滤器。

千万别在不可信的值上使用safe过滤器，例如用户在表单中输入的文本。此外我们亦可以自定义过滤函数然后传入模板中使用。

**自定义过滤器：**

```python
from flask import Markup

@app.template_filter()
def musical(s):
return s + Markup("&#9835")
```

亦可以在app.template_filter()装饰器里用name设置自定义过滤器的名称。

**3.控制结构**

Jinja2提供了多种控制结构，可用来改变模板的渲染流程。本节通过简单的例子介绍其中最有用的一些控制结构。下面这个例子展示如何在模板中使用条件判断语句：

```jinja2
{% if user %}
    Hello, {{ user }}!
{% else %}
    Hello, Stranger!
{% endif %}
```

另一种常见需求是在模板中渲染一组元素。下例展示了如何使用for循环实现这一需求：

```jinja2
<ul>
    {% for comment in comments %}
        <li>{{ comment }}</li>
    {% endfor %}
</ul>
```

常见的Jinja2中for循环特殊变量：

| 变量名         | 说明                          |
| -------------- | ----------------------------- |
| loop.index     | 当前迭代数（从1开始计数）     |
| loop.index0    | 当前迭代数（从0开始计数）     |
| loop.revindex  | 当前反向迭代数（从1开始计数） |
| loop.revindex0 | 当前反向迭代数（从0开始计数） |
| loop.first     | 如果是第一个元素，则为True    |
| loop.last      | 如果是最后一个元素，则为True  |
| loop.preitem   | 上一个迭代的条目              |
| loop.nextitem  | 下一个迭代的条目              |
| loop.length    | 序列包含的元素数量            |

Jinja2还支持宏。宏类似于Python代码中的函数。例如：

```jinja2
{% macro render_comment(comment) %}
    <li>{{ comment }}</li>
{% endmacro %}

<ul>
    {% for comment in comments %}
        {{ render_comment(comment) }}
    {% endfor %}
</ul>
```

为了重复使用宏，可以把宏保存在单独的文件中，然后在需要使用的模板中导入：

```jinja2
{% import 'macros.html' as macros %}
<ul>
    {% for comment in comments %}
        {{ macros.render_comment(comment) }}
    {% endfor %}
</ul>
```

需要在多处重复使用的模板代码片段可以写入单独的文件，再插入其他模板之中，以避免重复：

```jinja2
{% include 'common.html' %}
```

另一种重复使用代码的强大方式是模板继承，这类似于Python代码中的类继承。首先，创建一个名为base.html的基模板：

```jinja2
<html>
<head>
    {% block head %}
    <title>{% block title %}{% endblock %} - My Application</title>
    {% endblock %}
</head>
<body>
    {% block body %}
    {% endblock %}
</body>
</html>
```

基模板中定义的区块可在衍生模板中覆盖。Jinja2使用block和endblock指令在基模板中定义内容区块。在本例中，我们定义了名为head、title和body的区块。注意，title包含在head中。下面这个示例是基模板的衍生模板：

```jinja2
{% extends "base.html" %}
{% block title %}Index{% endblock %}
{% block head %}
    {{ super() }}
    <style>
    </style>
{% endblock %}
{% block body %}
<h1>Hello, World!</h1>
{% endblock %}
```

extends指令声明这个模板衍生自base.html。在extends指令之后，基模板中的3个区块被重新定义，模板引擎会将其插入适当的位置。如果基模板和衍生模板中的同名区块中都有内容，衍生模板中的内容将显示出来。在衍生模板的区块里可以调用super()，引用基模板中同名区块里的内容。上例中的head区块就是这么做的。

**4.上下文**

模板上下文包含了很多变量，其中包括我们调用render_template()函数时手动传入的变量以及Flask默认传入的变量。

**内置上下文变量：**

Flask在模板上下文中提供了一些内置变量，可以在模板中直接使用，如下所示：

| 变量    | 说明                                           |
| ------- | ---------------------------------------------- |
| config  | 当前的配置对象                                 |
| request | 当前的请求对象，在已激活的请求环境下可用       |
| session | 当前的会话对象，在已激活的请求环境下可用       |
| g       | 与请求绑定的全局变量，在已激活的请求环境下可用 |

**自定义上下文变量：**

如果多个模板都需要使用同一变量，那么比起在多个视图函数中重复传人，更好的方法是 能够设置一个模板全局变量。Flask提供了一个app.context_processor装饰器，可以用来注册模板上下文处理函数，它可以帮我们完成统一传入变量的工作。模板上下文处理函数需要返回一个包含变量键值对的字典，如下：

```python
@app.context_processor
def inject_foo():
    foo = "I am foo"
    return dict(foo=foo)
```

这样当我们渲染任意一个模板的时候，所有使用app.context_processor装饰器装饰的函数均会执行，这些函数的返回值会被添加到模板中，供我们直接在模板中使用。

**5.全局对象**

全局对象是指在所有的模板中都可以直接使用的对象，包括在模板中导入的模板。

**内置全局函数：**

Jinja2在模板中默认提供了一些全局函数，常用的三个如下：

| 函数                                    | 说明                                                         |
| --------------------------------------- | ------------------------------------------------------------ |
| range([start, ]stop[, step])            | 和Python中的range()用法相同                                  |
| lipsum(n=5, html=True, min=20, max=100) | 生成随即文本，可以在测试时用来填充页面。默认生成5段HTML文本，每段包含20~100个单词 |
| dict(**items)                           | 和Python中的dict用法相同                                     |

Flask内置的模板全局函数，如下：

| 函数                   | 说明                    |
| ---------------------- | ----------------------- |
| url_for()              | 用于生成URL的函数       |
| get_flashed_messages() | 用于获取flash消息的函数 |

**自定义全局函数：**

```python
@app.template_global()
def bar():
    return "I am bar"
```

默认使用函数的原名称传入模板，在app.template_global()装饰器中使用name参数可以指定一个自定义名称。

**6.测试器**

在Jinja2中，测试器是一些用来测试变量或表达式，返回布尔值的特殊函数。例如：

```jinja2
{% if age is number %}
    {{ age * 365 }}
{% else %}
	无效的数字
{% endif %}
```

**内置测试器：**

常见的测试器如下：

| 测试器                | 说明                                       |
| --------------------- | ------------------------------------------ |
| callable(object)      | 判断对象是否可被调用                       |
| defined(value)        | 判断变量是否被定义                         |
| undefined(value)      | 判断变量是否未定义                         |
| none(value)           | 判断变量是否为None                         |
| number(value)         | 判断变量是否为数字                         |
| string(value)         | 判断变量是否为字符串                       |
| sequence(value)       | 判断变量是否是序列，比如字符串、列表、元组 |
| iterable(value)       | 判断变量是否可迭代                         |
| mapping(value)        | 判断变量是否是匹配对象，比如字典           |
| sameas(value, orther) | 判断变量与other是否指向相同的内存地址      |

在使用测试器时，is的左侧是测试器函数的第一个参数(value)，其他参数可以添加括号传入，也可以在右侧使用空格连接，以sameas为例：

```jinja2
{% if foo is sameas(bar) %}
// ==
{% if foo is sameas bar %}
```

**自定义测试器：**

```python
@app.template_test()
def baz(n):
    if n == "baz":
        return True
    return False
```

测试器的名称默认为函数名称，你仍然可以进自定义名称。测试器函数需要接收被测试的值作为输入，返回布尔值。

#### Flask-Boostrap

Bootstrap是Twitter开发的一个开源Web框架，它提供的用户界面组件可用于创建整洁且具有吸引力的网页，而且兼容所有现代的桌面和移动平台Web浏览器。

Bootstrap是客户端框架，因此不会直接涉及服务器。服务器需要做的只是提供引用了Bootstrap层叠样式表（CSS，cascading style sheet）和JavaScript文件的HTML响应，并在HTML、CSS和JavaScript代码中实例化所需的用户界面元素。这些操作最理想的执行场所就是模板。

要想在应用中集成Bootstrap，最直接的方法是根据Bootstrap文档中的说明对HTML模板进行必要的改动。不过，这个任务使用Flask 扩展处理要简单得多，而且相关的改动不会导致主逻辑凌乱不堪。

我们要使用的扩展是Flask-Bootstrap，它可以使用pip安装：

```shell
(venv) $ pip install flask-bootstrap
```

Flask扩展在创建应用实例时初始化。以下是Flask-Bootstrap的初始化方式。

```python
from flask_bootstrap import Bootstrap
# ...
bootstrap = Bootstrap(app)   # 还有另外一种初始化的方式
```

初始化Flask-Bootstrap之后，就可以在应用中使用一个包含所有Bootstrap文件和一般结构的基模板。应用利用Jinja2的模板继承机制来扩展这个基模板。下面是把user.html改写为衍生模板后的新版本：

```jinja2
{% extends "bootstrap/base.html" %}

{% block title %}Flasky{% endblock %}

{% block navbar %}
<div class="navbar navbar-inverse" role="navigation">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle"
            data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="/">Flasky</a>
        </div>
        <div class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li><a href="/">Home</a></li>
            </ul>
        </div>
    </div>
</div>
{% endblock %}

{% block content %}
<div class="container">
    <div class="page-header">
        <h1>Hello, {{ name }}!</h1>
    </div>
</div>
{% endblock %}
```

Jinja2中的extends指令从Flask-Bootstrap中导入bootstrap/base.html，从而实现模板继承。Flask-Bootstrap的基模板提供了一个网页骨架，引入了Bootstrap的所有CSS和JavaScript文件。

上面这个user.html模板定义了3个区块，分别名为title、navbar和content。这些区块都是基模板提供的，可在衍生模板中重新定义。title区块的作用很明显，其中的内容会出现在渲染后的HTML文档头部，放在\<title>标签中。navbar和content这两个区块分别表示页面中的导航栏和主体内容。

Flask-Bootstrap的base.html模板还定义了很多其他区块，都可在衍生模板中使用。下表列出了所有可用的区块。

| 区块名       | 说明                     |
| ------------ | ------------------------ |
| doc          | 整个HTML文档             |
| html_attribs | \<html>标签的属性        |
| html         | \<html>标签中的内容      |
| head         | \<title>标签中的内容     |
| metas        | 一组\<meta>标签          |
| styles       | CSS声明                  |
| body_attribs | \<body>标签的属性        |
| body         | \<body>标签中的内容      |
| navbar       | 用户定义的导航栏         |
| content      | 用户自定义的页面内容     |
| scripts      | 文档底部的JavaScript声明 |

表3-2中的很多区块都是Flask-Bootstrap自用的，如果直接覆盖可能会导致一些问题。例如，Bootstrap的CSS和JavaScript文件在styles和scripts区块中声明。如果应用需要向已经有内容的块中添加新内容，必须使用Jinja2提供的super()函数。例如，如果要在衍生模板中添加新的JavaScript文件，需要这么定义scripts区块：

```jinja2
{% block scripts %}
{{ super() }}
<script type="text/javascript" src="my-script.js"></script>
{% endblock %}
```

#### 自定义错误页面

如果你在浏览器的地址栏中输入了无效的路由，会看到一个状态码为404的错误页面。与使用Bootstrap的页面相比，现在这个错误页面太简陋、平庸，而且与现有页面不一致。

像常规路由一样，Flask允许应用使用模板自定义错误页面。最常见的错误代码有两个： 404，客户端请求未知页面或路由时显示；500，应用有未处理的异常时显示。使用app.errorhandler装饰器为这两个错误提供自定义的处理函数。

```python
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
```

与视图函数一样，错误处理函数也返回一个响应。此外，错误处理函数还要返回与错误对应的数字状态码。状态码可以直接通过第二个返回值指定。

错误处理函数中引用的模板也需要我们编写。这些模板应该和常规页面使用相同的布局，因此要有一个导航栏和显示错误消息的页头。

编写这些模板最直接的方法是分别创建templates/404.html和templates/500.html，然后利用Jinja2继承base.html模板。

```jinja2
// templates/base.html
{% extends "bootstrap/base.html" %}

{% block title %}Flasky{% endblock %}

{% block navbar %}
<div class="navbar navbar-inverse" role="navigation">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle"
             data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="/">Flasky</a>
        </div>
        <div class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li><a href="/">Home</a></li>
            </ul>
        </div>
    </div>
</div>
{% endblock %}

{% block content %}
<div class="container">
    {% block page_content %}{% endblock %}
</div>
{% endblock %}
```

```jinja2
// templates/errors/404.html
{% extends "base.html" %}

{% block title %}Flasky - Page Not Found{% endblock %}

{% block page_content %}
<div class="page-header">
    <h1>Not Found</h1>
</div>
{% endblock %}
```

#### 链接：url_for()

任何具有多个路由的应用都需要可以连接不同页面的链接，例如导航栏。在模板中直接编写简单路由的URL链接不难，但对于包含可变部分的动态路由，在模板中构建正确的URL就很困难了。而且，直接编写URL会对代码中定义的路由产生不必要的依赖关系。如果重新定义路由，模板中的链接可能会失效。为了避免这些问题，Flask提供了url_for()辅助函数，它使用应用的URL映射中保存的信息生成URL。

url_for()函数最简单的用法是以视图函数名（或者app.add_url_route()定义路由时使用的端点名）作为参数，返回对应的URL。例如，在当前版本的hello.py应用中调用url_for('index')得到的结果是/，即应用的根URL。调用url_for('index', _external=True)返回的则是绝对地址，在这个示例中是http://localhost:5000/。

使用url_for()生成动态URL时，将动态部分作为关键字参数传入。例如，url_for('user', name='john', _external=True)的返回结果是http://localhost:5000/user/john。传给url_for()的关键字参数不仅限于动态路由中的参数，非动态的参数也会添加到查询字符串中。例如，url_for('user', name='john', page=2, version=1)的返回结果是/user/ john?page=2&version=1。

#### 静态文件

Web应用不是仅由Python代码和模板组成。多数应用还会使用静态文件，例如模板中HTML代码引用的图像、JavaScript源码文件和CSS。

默认设置下，Flask在应用根目录中名为static的子目录中寻找静态文件。如果需要，可在static文件夹中使用子文件夹存放文件。服务器收到映射到static路由上的URL后，生成的响应包含文件系统中对应文件里的内容。

下面展示了如何在应用的基模板中引入favicon.ico图标。这个图标会显示在浏览器的地址栏中。

```jinja2
{% block head %}
{{ super() }}
<link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}"
    type="image/x-icon">
<link rel="icon" href="{{ url_for('static', filename='favicon.ico') }}"
    type="image/x-icon">
{% endblock %}
```

这个图标的声明插入head区块的末尾。注意，为了保留基模板中这个区块里的原始内容，我们调用了super()。

#### 本地化日期和时间

如果Web应用的用户来自世界各地，那么处理日期和时间可不是一个简单的任务。

服务器需要统一时间单位，这和用户所在的地理位置无关，所以一般使用协调世界时（UTC，coordinated universal time）。不过用户看到UTC格式的时间会感到困惑，他们更希望看到当地时间，而且采用当地惯用的格式。

要想在服务器上只使用UTC时间，一个优雅的解决方案是，把时间单位发送给Web浏览器，转换成当地时间，然后用JavaScript渲染。Web浏览器可以更好地完成这一任务，因为它能获取用户计算机中的时区和区域设置。

有一个使用JavaScript开发的优秀客户端开源库，名为Moment.js，它可以在浏览器中渲染日期和时间。Flask-Moment是一个Flask扩展，能简化把Moment.js集成到Jinja2模板中的过程。Flask-Moment使用pip安装：

```shell
(venv) $ pip install flask-moment
```

```python
from flask_moment import Moment
moment = Moment(app)   # 还有另一种初始化的方法
```

除了Moment.js，Flask-Moment还依赖jQuery.js。因此，要在HTML文档的某个地方引入这两个库，可以直接引入，这样可以选择使用哪个版本，也可以使用扩展提供的辅助函数，从内容分发网络（CDN，content delivery network）中引入通过测试的版本。Bootstrap已经引入了jQuery.js，因此只需引入Moment.js即可。除了Moment.js，Flask-Moment还依赖jQuery.js。因此，要在HTML文档的某个地方引入这两个库，可以直接引入，这样可以选择使用哪个版本，也可以使用扩展提供的辅助函数，从内容分发网络（CDN，content delivery network）中引入通过测试的版本。Bootstrap已经引入了jQuery.js，因此只需引入Moment.js即可。

```jinja2
{% block scripts %}
{{ super() }}
{{ moment.include_moment() }}
{% endblock %}
```

为了处理时间戳，Flask-Moment向模板开放了moment对象。下面展示传入current_time以及如何渲染它。

```python
from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html',
                           current_time=datetime.utcnow())
```

```jinja2
<p>The local date and time is {{ moment(current_time).format('LLL') }}.</p>
<p>That was {{ moment(current_time).fromNow(refresh=True) }}</p>
```

format('LLL')函数根据客户端计算机中的时区和区域设置渲染日期和时间。参数决定了渲染的方式，从'L'到'LLLL'分别对应不同的复杂度。format()函数还可接受很多自定义的格式说明符。

第二行中的fromNow()渲染相对时间戳，而且会随着时间的推移自动刷新显示的时间。这个时间戳最开始显示为“a few seconds ago”，但设定refresh=True参数后，其内容会随着时间的推移而更新。如果一直待在这个页面，几分钟后会看到显示的文本变成“a minute ago”“2 minutes ago”，等等。

Flask-Moment实现了Moment.js的format()、fromNow()、fromTime()、calendar()、valueOf()和unix()等方法。

Flask-Moment渲染的时间戳可实现多种语言的本地化。语言可在模板中选择，方法是在引入Moment.js之后，立即把两个字母的语言代码传给locale()函数。例如，配置Moment.js使用中文简体的方式如下：

```jinja2
{% block scripts %}
{{ super() }}
{{ moment.include_moment() }}
{{ moment.locale('zh') }}
{% endblock %}
```

### Web表单

#### 介绍

前面编写的模板都是单向的，所有信息都从服务器流向用户。然而，对多数应用来说，还需要沿相反的方向流动信息，把用户提供的数据交给服务器来处理。

使用HTML可以创建Web表单，供用户填写信息。表单数据由Web浏览器提交给服务器，这一过程通常使用POST请求。对包含表单数据的POST请求来说，用户填写的信息通过request.form访问。

尽管Flask的请求对象提供的信息足以处理Web表单，但有些任务很单调，而且要重复操作。比如，生成表单的HTML代码和验证提交的表单数据（但是你需要知道在不用扩展的情况下如何处理）。

Flask-WTF扩展可以把处理Web表单的过程变成一种愉悦的体验。这个扩展对独立的WTForms包进行了包装，方便集成到Flask应用中。Flask-WTF及其依赖可使用pip安装：

```shell
(venv) $ pip install flask-wtf
```

#### 配置

与其他多数扩展不同，Flask-WTF无须在应用层初始化，但是它要求应用配置一个密钥。密钥是一个由随机字符构成的唯一字符串，通过加密或签名以不同的方式提升应用的安全性。Flask使用这个密钥保护用户会话，以防被篡改。每个应用的密钥应该不同，而且不能让任何人知道。

```python
app = Flask(__name__)
# 部署时密钥不应该直接写入源码，而要保存在环境变量中
app.config['SECRET_KEY'] = 'hard to guess string'   # 还有其他的配置方式
```

app.config字典可用于存储Flask、扩展和应用自身的配置变量。使用标准的字典句法就能把配置添加到app.config对象中。这个对象还提供了一些方法，可以从文件或环境中导入配置。

Flask-WTF之所以要求应用配置一个密钥，是为了防止表单遭到跨站请求伪造（CSRF，cross-site request forgery）攻击。恶意网站把请求发送到被攻击者已登录的其他网站时，就会引发CSRF攻击。Flask-WTF为所有表单生成安全令牌，存储在用户会话中。令牌是一种加密签名，根据密钥生成（这就是为什么要用成熟的且稳定质量有保证的扩展的原因，因为安全性得到了极大的保障，并且我们便不需要去处理这些东西）。

#### 定义表单类

使用Flask-WTF时，在服务器端，每个Web表单都由一个继承自FlaskForm的类表示。这个类定义表单中的一组字段，每个字段都用对象表示。字段对象可附属一个或多个验证函数。验证函数用于验证用户提交的数据是否有效。

```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
```

这个表单中的字段都定义为类变量，而各个类变量的值是相应字段类型的对象。在这个示例中，NameForm表单中有一个名为name的文本字段和一个名为submit的提交按钮。StringField类表示属性为type="text"的HTML\<input>元素。SubmitField类表示属性为type="submit"的HTML\<input>元素。字段构造函数的第一个参数是把表单渲染成HTML时使用的标注（label）。

WTForms支持的HTML标准字段如下表所示：

| 字段类型            | 说明                                |
| ------------------- | ----------------------------------- |
| BooleanField        | 复选框，值为True和False             |
| DateField           | 文本字段，值为datetime.data格式     |
| DateTimeField       | 文本字段，值为datetime.datetime格式 |
| DecimalField        | 文本字段，值为decimal.Decimal       |
| FileField           | 文件上传字段                        |
| HiddenField         | 隐藏的文本字段                      |
| MultipleFileField   | 多文件上传字段                      |
| FieldList           | 一组指定类型的字段                  |
| FormField           | 把一个表单作为字段嵌入另一个表单    |
| IntegerField        | 文本字段，值为整数                  |
| PasswordField       | 密码文本字段                        |
| RadioField          | 一组单选按钮                        |
| SelectField         | 下拉列表                            |
| SelectMultipleField | 下拉列表，可选择多个值              |
| SubmitField         | 表单提交按钮                        |
| StringField         | 文本字段                            |
| TextAreaField       | 多行文本字段                        |

WTForms内建的验证函数如下表，如果它们还不能满足，亦可以自定义验证函数：

| 验证函数      | 说明                                                   |
| ------------- | ------------------------------------------------------ |
| DataRequired  | 确保转换类型后字段中有数据                             |
| Email         | 验证电子邮件地址                                       |
| EqualTo       | 比较两个字段的值，常用于要求输入两次密码进行确认的情况 |
| InputRequired | 确保转换类型前字段中有数据                             |
| IPAddress     | 验证IPv4网络地址                                       |
| Length        | 验证输入字符串的长度                                   |
| MacAddress    | 验证MAC地址                                            |
| NumberRange   | 验证输入的值在数字范围之内                             |
| Optional      | 允许字段中没有输入，将跳过其他验证函数                 |
| Regexp        | 使用正则表达式验证输入值                               |
| URL           | 验证URL                                                |
| UUID          | 验证UUID                                               |
| AnyOf         | 确保输入值在一组可能的值中                             |
| NoneOf        | 确保输入值不在一组可能的值中                           |

#### 将表单渲染成HTML

表单字段是可调用的，在模板中调用后会渲染成HTML。假设视图函数通过form参数把一个NameForm实例传入模板，在模板中可以生成一个简单的HTML表单，如下所示：

```jinja2
<form method="POST">
    {{ form.hidden_tag() }}
    {{ form.name.label }} {{ form.name() }}
    {{ form.submit() }}
</form>
```

注意，除了name和submit字段，这个表单还有个form.hidden_tag()元素。这个元素生成一个隐藏的字段，供Flask-WTF的CSRF防护机制使用。

当然，这种方式渲染出的表单还很简陋。调用字段时传入的任何关键字参数都将转换成字段的HTML属性。例如，可以为字段指定id或class属性，然后为其定义CSS样式：

```jinja2
<form method="POST">
    {{ form.hidden_tag() }}
    {{ form.name.label }} {{ form.name(id='my-text-field') }}
    {{ form.submit() }}
</form>
```

即便能指定HTML属性，但按照这种方式渲染及美化表单的工作量还是很大，所以在条件允许的情况下，最好使用Bootstrap的表单样式。Flask-Bootstrap扩展提供了一个高层级的辅助函数，可以使用Bootstrap预定义的表单样式渲染整个Flask-WTF表单，而这些操作只需一次调用即可完成。使用Flask-Bootstrap，上述表单可以用下面的方式渲染：

```jinja2
{% import "bootstrap/wtf.html" as wtf %}
{{ wtf.quick_form(form) }}
```

wtf.quick_form()函数的参数为Flask-WTF表单对象，使用Bootstrap的默认样式渲染传入的表单。hello.py的完整模板如下所示：

```jinja2
{% extends "base.html" %}
{% import "bootstrap/wtf.html" as wtf %}

{% block title %}Flasky{% endblock %}

{% block page_content %}
<div class="page-header">
    <h1>Hello, {% if name %}{{ name }}{% else %}Stranger{% endif %}!</h1>
</div>
{{ wtf.quick_form(form) }}
{% endblock %}
```

#### 视图函数中处理表单

使用GET和POST请求方法处理Web表单：

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)
```

app.route装饰器中多出的methods参数告诉Flask，在URL映射中把这个视图函数注册为GET和POST请求的处理程序。如果没指定methods参数，则只把视图函数注册为GET请求的处理程序。

这里有必要把POST加入方法列表，因为更常使用POST请求处理表单提交。表单也可以通过GET请求提交，但是GET请求没有主体，提交的数据以查询字符串的形式附加到URL中，在浏览器的地址栏中可见。基于这个以及其他多个原因，处理表单提交几乎都使用POST请求。

局部变量name用于存放表单中输入的有效名字，如果没有输入，其值为None。如上述代码所示，我们在视图函数中创建了一个NameForm实例，用于表示表单。提交表单后，如果数据能被所有验证函数接受，那么validate_on_submit()方法的返回值为True，否则返回False。这个函数的返回值决定是重新渲染表单还是处理表单提交的数据。

用户首次访问应用时，服务器会收到一个没有表单数据的GET请求，所以validate_on_submit()将返回False。此时，if语句的内容将被跳过，对请求的处理只是渲染模板，并传入表单对象和值为None的name变量作为参数。用户会看到浏览器中显示了一个表单。

用户提交表单后，服务器会收到一个包含数据的POST请求。validate_on_submit()会调用名字字段上依附的DataRequired()验证函数。如果名字不为空，就能通过验证，validate_on_submit()返回True。现在，用户输入的名字可通过字段的data属性获取。在if语句中，把名字赋值给局部变量name，然后再把data属性设为空字符串，清空表单字段。因此，再次渲染这个表单时，各字段中将没有内容。最后一行调用render_template()函数渲染模板，但这一次参数name的值为表单中输入的名字，因此会显示一个针对该用户的欢迎消息。

#### 重定向和用户会话

前一版hello.py存在一个可用性问题。用户输入名字后提交表单，然后点击浏览器的刷新按钮，会看到一个莫名其妙的警告，要求在再次提交表单之前进行确认。之所以出现这种情况，是因为刷新页面时浏览器会重新发送之前发送过的请求。如果前一个请求是包含表单数据的POST请求，刷新页面后会再次提交表单。多数情况下，这并不是我们想执行的操作，因此浏览器才要求用户确认。

很多用户不理解浏览器发出的这个警告。鉴于此，最好别让Web应用把POST请求作为浏览器发送的最后一个请求。

这种需求的实现方式是，使用重定向作为POST请求的响应，而不是使用常规响应。重定向是一种特殊的响应，响应内容包含的是URL，而不是HTML代码的字符串。浏览器收到这种响应时，会向重定向的URL发起GET请求，显示页面的内容。这个页面的加载可能要多花几毫秒，因为要先把第二个请求发给服务器。除此之外，用户不会察觉到有什么不同。现在，前一个请求是GET请求，所以刷新命令能像预期的那样正常运作了。这个技巧称为Post/重定向/Get模式。

但这种方法又会引起另一个问题。应用处理POST请求时，可以通过form.name.data获取用户输入的名字，然而一旦这个请求结束，数据也就不见了。因为这个POST请求使用重定向处理，所以应用需要保存输入的名字，这样重定向后的请求才能获得并使用这个名字，从而构建真正的响应。

应用可以把数据存储在用户会话中，以便在请求之间“记住”数据。用户会话是一种私有存储，每个连接到服务器的客户端都可访问。

默认情况下，用户会话保存在客户端cookie中，使用前面设置的密钥加密签名。如果篡改了cookie的内容，签名就会失效，会话也将随之失效。

如下是index()视图函数的新版本，实现了重定向和用户会话：

```python
from flask import Flask, render_template, session, redirect, url_for

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))
```

应用的前一个版本在局部变量name中存储用户在表单中输入的名字。这个变量现在保存在用户会话中，即session['name']，所以在两次请求之间能记住输入的值。

#### 闪现消息

请求完成后，有时需要让用户知道状态发生了变化，可以是确认消息、警告或者错误提醒。一个典型例子是，用户提交有一项错误的登录表单后，服务器发回的响应重新渲染登录表单，并在表单上面显示一个消息，提示用户名或密码无效。Flask本身内置这个功能。如下所示，flash()函数可实现这种效果：

```python
from flask import Flask, render_template, session, redirect, url_for, flash

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html',
        form = form, name = session.get('name'))
```

仅调用flash()函数并不能把消息显示出来，应用的模板必须渲染这些消息。最好在基模板中渲染闪现消息，因为这样所有页面都能显示需要显示的消息。Flask把get_flashed_messages()函数开放给模板（全局函数之一），用于获取并渲染闪现消息，如下所示：

```jinja2
{% block content %}
<div class="container">
    {% for message in get_flashed_messages() %}
    <div class="alert alert-warning">
        <button type="button" class="close" data-dismiss="alert">&times;</button>
        {{ message }}
    </div>
    {% endfor %}

    {% block page_content %}{% endblock %}
</div>
{% endblock %}
```

这里使用了循环，因为在之前的请求循环中每次调用flash()函数时都会生成一个消息，所以可能有多个消息在排队等待显示。get_flashed_messages()函数获取的消息在下次调用时不会再次返回，因此闪现消息只显示一次，然后就消失了。

### 数据库

数据库按照一定规则保存应用的数据，应用再发起查询，取回所需的数据。Web应用最常使用基于关系模型的数据库，这种数据库也称为SQL数据库，因为它们使用结构化查询语言（SQL）。不过近年来文档数据库和键–值对数据库成了流行的替代选择，这两种数据库合称NoSQL数据库。

#### SQL数据库

关系型数据库把数据存储在表中，表为应用中不同的实体建模。例如，订单管理应用的数据库中可能有customers、products和orders等表。

表中的列数是固定的，行数是可变的。列定义表所表示的实体的数据属性。例如，customers表中可能有name、address、phone等列。表中的行定义部分或所有列对应的真实数据。

表中有个特殊的列，称为主键，其值为表中各行的唯一标识符。表中还可以有称为外键的列，引用同一个表或不同表中某一行的主键。行之间的这种联系称为关系，这正是关系型数据库模型的基础。

关系型数据库表之间的关系有：一对多、多对一、一对一以及多对多。Flask的扩展Flask-SQLAlchemy提供了方便的方式来构建这些关系（当然，这并不意味着就不去掌握比较麻烦的方式）

#### NoSQL数据库

所有不符合上节所述的关系模型的数据库统称为NoSQL数据库。NoSQL数据库一般使用集合代替表，使用文档代替记录。NoSQL数据库采用的设计方式使联结变得困难，所以多数根本不支持这种操作。

NoSQL数据库的表设计为直接按列存储，而不需要像SQL数据库那样创建多个表并设计它们之间的关系。

NoSQL这种结构的数据库，重命名角色的操作就变得很耗时，可能需要更新大量文档。使用NoSQL数据库当然也有好处。数据重复可以提升查询速度。列出用户及其角色的操作将很简单，因为无须联结。

#### 选择困难症

**使用SQL还是NoSQL**

SQL数据库擅于用高效且紧凑的形式存储结构化数据。这种数据库需要花费大量精力保证数据的一致性，需要考虑停电或硬件失效。为了达到这种程度的可靠性，关系型数据库采用一种称为ACID的范式，即atomicity（原子性）、consistency（一致性）、isolation（隔离性）和durability（持续性）。NoSQL数据库放宽了对ACID的要求，从而获得性能上的优势。

对中小型应用来说，SQL和NoSQL数据库都是很好的选择，而且性能相当。

**Python数据库框架**

大多数数据库引擎都有对应的Python包，包括开源包和商业包。Flask并不限制你使用何种类型的数据库包，因此你可以根据自己的喜好选择使用MySQL、Postgres、SQLite、Redis、MongoDB、CouchDB或DynamoDB。

如果这些都无法满足需求，还有一些数据库抽象层代码包供选择，例如SQLAlchemy和MongoEngine。你可以使用这些抽象包直接处理高等级的Python对象，而不用处理如表、文档或查询语言之类的数据库实体。

选择数据库框架时，要考虑很多因素。易用性、性能、可移植性、Flask集成度。基于以上因素，这里选择使用的数据库框架是Flask-SQLAlchemy，这个Flask扩展包装了SQLAlchemy框架。

#### 使用数据库扩展

Flask-SQLAlchemy是一个Flask扩展，简化了在Flask应用中使用SQLAlchemy的操作（配置之类的）。SQLAlchemy是一个强大的关系型数据库框架，支持多种数据库后台。SQLAlchemy提供了高层ORM，也提供了使用数据库原生SQL的低层功能。

```shell
(venv) $ pip install flask-sqlalchemy
```

在Flask-SQLAlchemy中，数据库使用URL指定。几种最流行的数据库引擎使用的URL格式如下所示：

| 数据库引擎            | URL                                         |
| --------------------- | ------------------------------------------- |
| MySQL                 | mysql://username:password@hostname/database |
| SQLite (Linux, macOS) | sqlite:////absolute/path/to/database        |
| SQLite (Windows)      | sqlite:///c:/absolute/path/to/database      |

在这些URL中，hostname表示数据库服务所在的主机，可以是本地主机（localhost），也可以是远程服务器。数据库服务器上可以托管多个数据库，因此database表示要使用的数据库名。如果数据库需要验证身份，使用username和password提供数据库用户的凭据。

SQLite数据库没有服务器，因此不用指定hostname、username和password。URL中的database是磁盘中的文件名。

应用使用的数据库URL必须保存到Flask配置对象的SQLALCHEMY_DATABASE_URI键中。Flask-SQLAlchemy文档还建议把SQLALCHEMY_TRACK_MODIFICATIONS键设为False，以便在不需要跟踪对象变化时降低内存消耗。其他配置选项的作用参阅Flask-SQLAlchemy的文档。

```python
import os 
from flask import flask-sqlalchemy

base_dir = os.path.abspath(os.path.dirname(__name__))

app = Flask(__name__)
# 还有其他进行配置的方法
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(base_dir, 'data.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db = SQLAlchemy(app)
```

db对象是SQLAlchemy类的实例，表示应用使用的数据库，通过它可获得Flask-SQLAlchemy提供的所有功能。

#### 定义模型

模型这个术语表示应用使用的持久化实体。在ORM中，模型一般是一个Python类，类中的属性对应于数据库表中的列。

Flask-SQLAlchemy创建的数据库实例为模型提供了一个基类以及一系列辅助类和辅助函数，可用于定义模型的结构。

```python
class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64, unique=True)
    
    def __repr__(self):
        return f"<Role {self.name}>"
        
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    
    def __repr__(self):
        return f"<User {self.name}>"
```

类变量\_\_tablename\_\_定义在数据库中使用的表名。如果没有定义\__tablename__，Flask-SQLAlchemy会使用一个默认名称，但默认的表名没有遵守流行的使用复数命名的约定，所以最好由我们自己来指定表名。其余的类变量都是该模型的属性，定义为db.Column类的实例。

db.Column类构造函数的第一个参数是数据库列和模型属性的类型。下表列出了一些可用的列类型以及在模型中使用的Python类型。

| 类型名       | Python类型         | 说明                                                  |
| ------------ | ------------------ | ----------------------------------------------------- |
| Integer      | int                | 普通整数，通常是32位                                  |
| SmallInteger | int                | 取值范围小的整数，通常是16位                          |
| BigInteger   | int或long          | 不限制精度的整数                                      |
| Float        | float              | 浮点数                                                |
| Numeric      | decimal.Decmial    | 定点数                                                |
| String       | str                | 变长字符串                                            |
| Text         | str                | 变长字符串，对较长或不限长度的字符串做了优化          |
| Unicode      | unicode            | 变长的Unicode字符串                                   |
| UnicodeText  | unicode            | 变长的Unicode字符串，对较长或不限长度的字符串做了优化 |
| Boolean      | bool               | 布尔值                                                |
| Date         | datetime.date      | 日期                                                  |
| Time         | datetime.time      | 时间                                                  |
| DateTime     | datetime.datetime  | 日期和时间                                            |
| Interval     | datetime.timedelta | 时间间隔                                              |
| Enum         | str                | 一组字符串                                            |
| PickleType   | 任何Python对象     | 自动使用Pickle序列化                                  |
| LargeBinary  | str                | 二进制blob                                            |

db.Column的其余参数指定属性的配置选项。最常用的SQLAlchemy列选项：

| 选项名      | 说明                                                         |
| ----------- | ------------------------------------------------------------ |
| primary_key | 如果设为True，列为表的主键                                   |
| unique      | 如果设为True，列不允许出现重复的值                           |
| index       | 如果设为True，为列创建索引，提升查询效率                     |
| nullable    | 如果设为True，列允许使用空值，如果设置为False，列不允许有空值 |
| default     | 为列定义默认值                                               |

Flask-SQLAlchemy要求每个模型都定义主键，这一列经常命名为id。虽然没有强制要求，但这两个模型都定义了\__repr()__方法，返回一个具有可读性的字符串表示模型，供调试和测试时使用。

#### 数据库表关系

关系型数据库使用关系把不同表中的行联系起来。关系有：一对多、多对一、一对一以及多对多。

```python
# 一对多
class Role(db.Model):
    # ...
    users = db.relationship('User', backref='role')

class User(db.Model):
    # ...
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
```

如上所示，关系使用users表中的外键连接两行。添加到User模型中的role_id列被定义为外键，就是这个外键建立起了关系。传给db.ForeignKey()的参数'roles.id'表明，这列的值是roles表中相应行的id值。

从“一”那一端可见，添加到Role模型中的users属性代表这个关系的面向对象视角。对于一个Role类的实例，其users属性将返回与角色相关联的用户组成的列表（即“多”那一端）。db.relationship()的第一个参数表明这个关系的另一端是哪个模型。如果关联的模型类在模块后面定义，可使用字符串形式指定。

db.relationship()中的backref参数向User模型中添加一个role属性，从而定义反向关系。通过User实例的这个属性可以获取对应的Role模型对象，而不用再通过role_id外键获取。

多数情况下，db.relationship()都能自行找到关系中的外键，但有时却无法确定哪一列是外键。例如，如果User模型中有两个或以上的列定义为Role模型的外键，SQLAlchemy就不知道该使用哪一列。如果无法确定外键，就要为db.relationship()提供额外的参数。表5-4列出了定义关系时常用的配置选项。

| 选项名        | 说明                                                         |
| ------------- | ------------------------------------------------------------ |
| backref       | 在关系的另一个模型中添加反向引用                             |
| primaryjoin   | 明确指定两个模型之间使用联结条件，只有在模棱两可的关系中需要指定 |
| lazy          |                                                              |
| uselist       | 如果设为False，不使用列表，而使用标量值                      |
| order_by      | 指定关系中记录的排序方式                                     |
| secondary     | 指定多对多关系中关联表的名称                                 |
| secondaryjoin | SQLAlchemy无法自行决定时，指定多对多关系中的二级联结条件     |

除了一对多之外，还有其他几种关系类型。一对一关系可以用前面介绍的一对多关系表示，但调用db.relationship()时要把uselist设为False，把“多”变成“一”。多对一关系也可使用一对多表示，对调两个表即可，或者把外键和db.relationship()都放在“多”这一侧。最复杂的关系类型是多对多，需要用到第三张表，这个表称为关联表（或联结表）。其他的亦可见HelloFlask目录中的文件。

#### 数据库操作

现在模型已经按照前面的数据库关系完成配置，可以随时使用了。学习使用模型的最好方法是在Python shell中实际操作。接下来将介绍最常用的数据库操作。shell使用flask shell命令启动。不过在执行这个命令之前，要把FLASK_APP环境变量设为hello.py。

**创建表**

首先，要让Flask-SQLAlchemy根据模型类创建数据库。db.create_all()函数将寻找所有db.Model的子类，然后在数据库中创建对应的表：

```shell
(venv) $ flask shell
>>> from hello import db
>>> db.create_all()
```

现在查看应用目录，你会发现有个名为data.sqlite的文件，文件名与配置中指定的一样。如果数据库表已经存在于数据库中，那么db.create_all()不会重新创建或者更新相应的表。如果修改模型后要把改动应用到现有的数据库中，这一行为会带来不便。更新现有数据库表的蛮力方式是先删除旧表再重新创建：

```shell
>>> db.drop_all()
>>> db.create_all()
```

遗憾的是，这个方法有个我们不想看到的副作用，它把数据库中原有的数据都销毁了。后面将介绍一种更好的数据库更新方式（migrate）。

**插入行**

创建一些角色和用户：

```python
>>> from hello import Role, User
>>> admin_role = Role(name='Admin')
>>> mod_role = Role(name='Moderator')
>>> user_role = Role(name='User')
>>> user_john = User(username='john', role=admin_role)
>>> user_susan = User(username='susan', role=user_role)
>>> user_david = User(username='david', role=user_role)
```

模型的构造函数接受的参数是使用关键字参数指定的模型属性初始值。注意，role属性也可使用，虽然它不是真正的数据库列，但却是一对多关系的高级表示。新建对象时没有明确设定id属性，因为在多数数据库中主键由数据库自身管理。现在这些对象只存在于Python中，还未写入数据库。因此，id尚未赋值：

```python
>>> print(admin_role.id)
None
>>> print(mod_role.id)
None
>>> print(user_role.id)
None
```

对数据库的改动通过数据库会话管理，在Flask-SQLAlchemy中，会话由db.session表示。准备把对象写入数据库之前，要先将其添加到会话中：

```python
>>> db.session.add(admin_role)
>>> db.session.add(mod_role)
>>> db.session.add(user_role)
>>> db.session.add(user_john)
>>> db.session.add(user_susan)
>>> db.session.add(user_david)
```

或者简写成这样

```python
>>> db.session.add_all([admin_role, mod_role, user_role,
...     user_john, user_susan, user_david])
```

为了把对象写入数据库，我们要调用commit()方法提交会话：

```python
>>> db.session.commit()
```

提交数据后再查看id属性，现在它们已经赋值了：

```python
>>> print(admin_role.id)
1
>>> print(mod_role.id)
2
>>> print(user_role.id)
3
```

数据库会话能保证数据库的一致性。提交操作使用原子方式把会话中的对象全部写入数据库。如果在写入会话的过程中发生了错误，那么整个会话都会失效。如果你始终把相关改动放在会话中提交，就能避免因部分更新导致的数据库不一致。

数据库会话也可回滚。调用db.session.rollback()后，添加到数据库会话中的所有对象都将还原到它们在数据库中的状态。

**修改行**

在数据库会话上调用add()方法也能更新模型。我们继续在之前的shell会话中进行操作，下面这个例子把"Admin"角色重命名为"Administrator"：

```python
>>> admin_role.name = 'Administrator'
>>> db.session.add(admin_role)
>>> db.session.commit()
```

**删除行**

数据库会话还有个delete()方法。下面这个例子把"Moderator"角色从数据库中删除：

```python
>>> db.session.delete(mod_role)
>>> db.session.commit()
```

注意，删除与插入和更新一样，提交数据库会话后才会执行。

**查询行**

Flask-SQLAlchemy为每个模型类都提供了query对象。最基本的模型查询是使用all()方法取回对应表中的所有记录：

```python
>>> Role.query.all()
[<Role 'Administrator'>, <Role 'User'>]
>>> User.query.all()
[<User 'john'>, <User 'susan'>, <User 'david'>]
```

使用过滤器可以配置query对象进行更精确的数据库查询。下面这个例子查找角色为"User"的所有用户：

```python
>>> User.query.filter_by(role=user_role).all()
[<User 'susan'>, <User 'david'>]
```

若想查看SQLAlchemy为查询生成的原生SQL查询语句，只需把query对象转换成字符串：

```python
>>> str(User.query.filter_by(role=user_role))
'SELECT users.id AS users_id, users.username AS users_username,
users.role_id AS users_role_id \nFROM users \nWHERE :param_1 = users.role_id'
```

如果你退出了shell会话，前面这些例子中创建的对象就不会以Python对象的形式存在，但在数据库表中仍有对应的行。如果打开一个新的shell会话，要从数据库中读取行，重新创建Python对象。下面这个例子发起一个查询，加载名为"User"的用户角色：

```python
>>> user_role = Role.query.filter_by(name='User').first()
```

注意，这里发起查询的不是all()方法，而是first()方法。all()方法返回所有结果构成的列表，而first()方法只返回第一个结果，如果没有结果的话，则返回None。因此，如果知道查询最多返回一个结果，就可以用这个方法。

filter_by()等过滤器在query对象上调用，返回一个更精确的query对象。多个过滤器可以一起调用，直到获得所需结果。

下面是常用的SQLAlchemy查询过滤器：

| 过滤器      | 说明                                             |
| ----------- | ------------------------------------------------ |
| filter()    | 把过滤器添加到原查询上，返回一个新查询           |
| filter_by() | 把等值过滤器添加到原查询上，返回一个新查询       |
| limit()     | 使用指定的值限制原查询返回的结果数量，返回新查询 |
| offset()    | 偏移原查询返回的结果，返回一个新查询             |
| order_by()  | 根据指定条件对原查询结果进行排序，返回一个新查询 |
| group_by()  | 根据指定条件对原查询结果进行分组，返回一个新查询 |

在查询上应用指定的过滤器后，调用all()方法将执行查询，以列表的形式返回结果。除了all()方法之外，还有其他方法能触发查询执行。下面列出最常用的SQLAlchemy查询执行方法：

| 方法         | 说明                                                         |
| ------------ | ------------------------------------------------------------ |
| all()        | 以列表形式返回查询的所有结果                                 |
| first()      | 返回查询的第一个结果，如果没有结果，则返回None               |
| first_or_404 | 返回查询的第一个结果，如果没有结果                           |
| get()        | 返回指定主键对应的行，如果没有对应的行，则返回None           |
| get_or_404   | 返回指定主键对应的行，如果没找到指定的主键，则终止请求，返回404错误响应 |
| count()      | 返回查询结果的数量                                           |
| paginate()   | 返回一个Paginate对象，包含指定范围内的结果                   |

关系与查询的处理方式类似。下面这个例子分别从关系的两端查询角色和用户之间的一对多关系：

```python
>>> users = user_role.users
>>> users
[<User 'susan'>, <User 'david'>]
>>> users[0].role
<Role 'User'>
```

这个例子中的user_role.users查询有个小问题。执行user_role.users表达式时，隐式的查询会调用all()方法，返回一个用户列表。此时，query对象是隐藏的，无法指定更精确的查询过滤器。就这个示例而言，返回一个按照字母顺序排列的用户列表可能更好。在示例5-4中，我们修改了关系的设置，加入了lazy='dynamic'参数，从而禁止自动执行查询。

```python
class Role(db.Model):
    # ...
    users = db.relationship('User', backref='role', lazy='dynamic')
    # ...
```

这样配置关系之后，user_role.users将返回一个尚未执行的查询，因此可以在其上添加过滤器：

```python
>>> user_role.users.order_by(User.username).all()
[<User 'david'>, <User 'susan'>]
>>> user_role.users.count()
2
```

#### 视图函数中操作数据库

前面介绍的数据库操作可以直接在视图函数中进行。下面是首页路由的新版本，把用户输入的名字记录到数据库中。

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',
        form=form, name=session.get('name'),
        known=session.get('known', False))
```

在这个修改后的版本中，提交表单后，应用会使用filter_by()查询过滤器在数据库中查找提交的名字。变量known被写入用户会话中，因此重定向之后，可以把数据传给模板，用于显示自定义的欢迎消息。注意，为了让应用正常运行，必须按照前面介绍的方法，在Python shell中创建数据库表。

对应的模板新版本如下所示。这个模板使用known参数在欢迎消息中加入了第二行，从而对已知用户和新用户显示不同的内容。

```jinja2
{% extends "base.html" %}
{% import "bootstrap/wtf.html" as wtf %}

{% block title %}Flasky{% endblock %}

{% block page_content %}
<div class="page-header">
    <h1>Hello, {% if name %}{{ name }}{% else %}Stranger{% endif %}!</h1>
    {% if not known %}
    <p>Pleased to meet you!</p>
    {% else %}
    <p>Happy to see you again!</p>
    {% endif %}
</div>
{{ wtf.quick_form(form) }}
{% endblock %}
```

#### 集成Python Shell

每次启动shell会话都要导入数据库实例和模型，这真是份枯燥的工作。为了避免一直重复导入，我们可以做些配置，让flask shell命令自动导入这些对象。

若想把对象添加到导入列表中，必须使用app.shell_context_processor装饰器创建并注册一个shell上下文处理器，如下所示：

```python
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)
```

这个shell上下文处理器函数返回一个字典，包含数据库实例和模型。除了默认导入的app之外，flask shell命令将自动把这些对象导入shell.

```python
$ flask shell
>>> app
<Flask 'hello'>
>>> db
<SQLAlchemy engine='sqlite:////home/flask/flasky/data.sqlite'>
>>> User
<class 'hello.User'>
```

#### 实现数据库迁移

在开发应用的过程中，你会发现有时需要修改数据库模型，而且修改之后还要更新数据库。仅当数据库表不存在时，Flask-SQLAlchemy才会根据模型创建。因此，更新表的唯一方式就是先删除旧表，但是这样做会丢失数据库中的全部数据。

更新表更好的方法是使用数据库迁移框架。源码版本控制工具可以跟踪源码文件的变化；类似地，数据库迁移框架能跟踪数据库模式的变化，然后以增量的方式把变化应用到数据库中。

SQLAlchemy的开发人员编写了一个迁移框架，名为Alembic。除了直接使用Alembic之外，Flask应用还可使用Flask-Migrate扩展。这个扩展是对Alembic的轻量级包装，并与flask命令做了集成。

**创建迁移仓库**

```shell
(venv) $ pip install flask-migrate
```

```python
from flask_migrate import Migrate

# ...

migrate = Migrate(app, db)
```

为了开放数据库迁移相关的命令，Flask-Migrate添加了flask db命令和几个子命令。在新项目中可以使用init子命令添加数据库迁移支持：

```shell
(venv) $ flask db init
  Creating directory /home/flask/flasky/migrations...done
  Creating directory /home/flask/flasky/migrations/versions...done
  Generating /home/flask/flasky/migrations/alembic.ini...done
  Generating /home/flask/flasky/migrations/env.py...done
  Generating /home/flask/flasky/migrations/env.pyc...done
  Generating /home/flask/flasky/migrations/README...done
  Generating /home/flask/flasky/migrations/script.py.mako...done
  Please edit configuration/connection/logging settings in
  '/home/flask/flasky/migrations/alembic.ini' before proceeding.
```

这个命令会创建migrations目录，所有迁移脚本都存放在这里。如果你是通过git checkout检出示例项目的，那么无须做这一步，因为GitHub仓库中已有迁移仓库。数据库迁移仓库中的文件要和应用的其他文件一起纳入版本控制。

**创建迁移脚本**

在Alembic中，数据库迁移用迁移脚本表示。脚本中有两个函数，分别是upgrade()和downgrade()。upgrade()函数把迁移中的改动应用到数据库中，downgrade()函数则将改动删除。Alembic具有添加和删除改动的能力，意味着数据库可重设到修改历史的任意一点。

我们可以使用revision命令手动创建Alembic迁移，也可使用migrate命令自动创建。手动创建的迁移只是一个骨架，upgrade()和downgrade()函数都是空的，开发者要使用Alembic提供的Operations对象指令实现具体操作。自动创建的迁移会根据模型定义和数据库当前状态之间的差异尝试生成upgrade()和downgrade()函数的内容。

自动创建的迁移不一定总是正确的，有可能会漏掉一些细节。比如说我们重命名了一列，自动生成的迁移可能会把这当作删除了一列，然后又新增了一列。如果原封不动地使用自动生成的迁移，这一列中的数据就会丢失！鉴于此，自动生成迁移脚本后一定要进行检查，把不准确的部分手动改过来。

使用Flask-Migrate管理数据库模式变化的步骤如下。

(1)对模型类做必要的修改。

(2)执行flask db migrate命令，自动创建一个迁移脚本。

(3)检查自动生成的脚本，根据对模型的实际改动进行调整。

(4)把迁移脚本纳入版本控制。

(5)执行flask db upgrade命令，把迁移应用到数据库中。

flask db migrate子命令用于自动创建迁移脚本：

```shell
(venv) $ flask db migrate -m "initial migration"
INFO  [alembic.migration] Context impl SQLiteImpl.
INFO  [alembic.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate] Detected added table 'roles'
INFO  [alembic.autogenerate] Detected added table 'users'
INFO  [alembic.autogenerate.compare] Detected added index
'ix_users_username' on '['username']'
  Generating /home/flask/flasky/migrations/versions/1bc
  594146bb5_initial_migration.py...done
```

**更新数据库**

检查并修正好迁移脚本之后，执行flask db upgrade命令，把迁移应用到数据库中：

```shell
(venv) $ flask db upgrade
INFO  [alembic.migration] Context impl SQLiteImpl.
INFO  [alembic.migration] Will assume non-transactional DDL.
INFO  [alembic.migration] Running upgrade None -> 1bc594146bb5, initial migration
```

对第一个迁移来说，其作用与调用db.create_all()方法一样。但在后续的迁移中，flask db upgrade命令能把改动应用到数据库中，且不影响其中保存的数据。

如果你按照之前的说明操作过，那么已经使用db.create_all()函数创建了数据库文件。此时，flask db upgrade命令将失败，因为它试图创建已经存在的数据库表。一种简单的处理方法是，把data.sqlite数据库文件删掉，然后执行flask db upgrade命令，通过迁移框架重新创建数据库。另一种方法是不执行flask db upgrade命令，而是使用flask db stamp命令把现有数据库标记为已更新。

**添加几个迁移**

在开发项目的过程中，时常要修改数据库模型。如果使用迁移框架管理数据库，必须在迁移脚本中定义所有改动，否则改动将不可复现。修改数据库的步骤与创建第一个迁移类似。

(1)对数据库模型做必要的修改。

(2)执行flask db migrate命令，生成迁移脚本。

(3)检查自动生成的脚本，改正不准确的地方。

(4)执行flask db upgrade命令，把改动应用到数据库中。

实现一个功能时，可能要多次修改数据库模型才能得到预期结果。如果前一个迁移还未提交到源码控制系统中，可以继续在那个迁移中修改，以免创建大量无意义的小迁移脚本。在前一个迁移脚本的基础上修改的步骤如下。

(1)执行flask db downgrade命令，还原前一个脚本对数据库的改动（注意，这可能导致部分数据丢失）。

(2)删除前一个迁移脚本，因为现在已经没什么用了。

(3)执行flask db migrate命令生成一个新的数据库迁移脚本。这个迁移脚本除了前面删除的那个脚本中的改动之外，还包括这一次对模型的改动。

(4)根据前面的说明，检查并应用迁移脚本。

数据库设计和用法相关的话题十分重要，有大量相关的图书。这里介绍的还仅仅是皮毛，对于关系型数据库，推荐熟练掌握MySQL数据库。

### RESTful APIs

本篇教程为：[Designing a RESTful API with Python and Flask](http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask) ，作者是 **Miguel Grinberg** 。搬运过来，并且其中某些代码因Python过渡到3的原因无法运行，因此进行了更改。

#### 什么是REST？

六条设计规范定义了一个 REST 系统的特点:

- **客户端-服务器**: 客户端和服务器之间隔离，服务器提供服务，客户端进行消费。
- **无状态**: 从客户端到服务器的每个请求都必须包含理解请求所必需的信息。换句话说， 服务器不会存储客户端上一次请求的信息用来给下一次使用。
- **可缓存**: 服务器必须明示客户端请求能否缓存。
- **分层系统**: 客户端和服务器之间的通信应该以一种标准的方式，就是中间层代替服务器做出响应的时候，客户端不需要做任何变动。
- **统一的接口**: 服务器和客户端的通信方法必须是统一的。
- **按需编码**: 服务器可以提供可执行代码或脚本，为客户端在它们的环境中执行。这个约束是唯一一个是可选的。

#### 设计web service

**什么是一个 RESTful 的 web service？**

REST 架构的最初目的是适应万维网的 HTTP 协议。

RESTful web services 概念的核心就是“资源”。 资源可以用 [URI](https://en.wikipedia.org/wiki/Uniform_resource_identifier) 来表示。客户端使用 HTTP 协议定义的方法来发送请求到这些 URIs，当然可能会导致这些被访问的”资源“状态的改变。

HTTP 标准的方法有如下:

```
==========  =====================  ==================================
HTTP 方法   行为                   示例
==========  =====================  ==================================
GET         获取资源的信息         http://example.com/api/orders
GET         获取某个特定资源的信息 http://example.com/api/orders/123
POST        创建新资源             http://example.com/api/orders
PUT         更新资源               http://example.com/api/orders/123
DELETE      删除资源               http://example.com/api/orders/123
==========  ====================== ==================================
```

REST 设计不需要特定的数据格式。在请求中数据可以以 [JSON](http://en.wikipedia.org/wiki/JSON) 形式, 或者有时候作为 url 中查询参数项。

**设计一个简单的 web service**

坚持 REST 的准则设计一个 web service 或者 API 的任务就变成一个标识资源被展示出来以及它们是怎样受不同的请求方法影响的练习。

比如说，我们要编写一个待办事项应用程序而且我们想要为它设计一个 web service。要做的第一件事情就是决定用什么样的根 URL 来访问该服务。例如，我们可以通过这个来访问:

http://[hostname]/todo/api/v1.0/

在这里我已经决定在 URL 中包含应用的名称以及 API 的版本号。在 URL 中包含应用名称有助于提供一个命名空间以便区分同一系统上的其它服务。在 URL 中包含版本号能够帮助以后的更新，如果新版本中存在新的和潜在不兼容的功能，可以不影响依赖于较旧的功能的应用程序。

下一步骤就是选择将由该服务暴露(展示)的资源。这是一个十分简单地应用，我们只有任务，因此在我们待办事项中唯一的资源就是任务。

我们的任务资源将要使用 HTTP 方法如下:

```
==========  ===============================================  =============================
HTTP 方法   URL                                              动作
==========  ===============================================  ==============================
GET         http://[hostname]/todo/api/v1.0/tasks            检索任务列表
GET         http://[hostname]/todo/api/v1.0/tasks/[task_id]  检索某个任务
POST        http://[hostname]/todo/api/v1.0/tasks            创建新任务
PUT         http://[hostname]/todo/api/v1.0/tasks/[task_id]  更新任务
DELETE      http://[hostname]/todo/api/v1.0/tasks/[task_id]  删除任务
==========  ================================================ =============================
```

我们定义的任务有如下一些属性:

- **id**: 任务的唯一标识符。数字类型。
- **title**: 简短的任务描述。字符串类型。
- **description**: 具体的任务描述。文本类型。
- **done**: 任务完成的状态。布尔值。

目前为止关于我们的 web service 的设计基本完成。剩下的事情就是实现它！

#### 实现RESTful services

**使用 Python 和 Flask 实现 RESTful services**

使用 Flask 构建 web services 是十分简单地，比我在 [Mega-Tutorial](http://www.pythondoc.com/flask-mega-tutorial/index.html) 中构建的完整的服务端的应用程序要简单地多。

在 Flask 中有许多扩展来帮助我们构建 RESTful services，但是在我看来这个任务十分简单，没有必要使用 Flask 扩展。

我们 web service 的客户端需要添加、删除以及修改任务的服务，因此显然我们需要一种方式来存储任务。最直接的方式就是建立一个小型的数据库，但是数据库并不是本文的主体。学习在 Flask 中使用合适的数据库，我强烈建议阅读 [Mega-Tutorial](http://www.pythondoc.com/flask-mega-tutorial/index.html)。

这里我们直接把任务列表存储在内存中，因此这些任务列表只会在 web 服务器运行中工作，在结束的时候就失效。 这种方式只是适用我们自己开发的 web 服务器，不适用于生产环境的 web 服务器， 这种情况一个合适的数据库的搭建是必须的。

我们现在来实现 web service 的第一个入口:

```python
from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)
```

正如你所见，没有多大的变化。我们创建一个任务的内存数据库，这里无非就是一个字典和数组。数组中的每一个元素都具有上述定义的任务的属性。

取代了首页，我们现在拥有一个 get_tasks 的函数，访问的 URI 为 /todo/api/v1.0/tasks，并且只允许 GET 的 HTTP 方法。

这个函数的响应不是文本，我们使用 JSON 数据格式来响应，Flask 的 jsonify 函数从我们的数据结构中生成。

使用网页浏览器来测试我们的 web service 不是一个最好的注意，因为网页浏览器上不能轻易地模拟所有的 HTTP 请求的方法。相反，我们会使用 curl。如果你还没有安装 curl 的话，请立即安装它。

通过执行 app.py，启动 web service。接着打开一个新的控制台窗口，运行以下命令:

```bash
$ curl -i http://localhost:5000/todo/api/v1.0/tasks
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 294
Server: Werkzeug/0.8.3 Python/2.7.3
Date: Mon, 20 May 2013 04:53:53 GMT

{
  "tasks": [
    {
      "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
      "done": false,
      "id": 1,
      "title": "Buy groceries"
    },
    {
      "description": "Need to find a good Python tutorial on the web",
      "done": false,
      "id": 2,
      "title": "Learn Python"
    }
  ]
}
```

我们已经成功地调用我们的 RESTful service 的一个函数！

现在我们开始编写 GET 方法请求我们的任务资源的第二个版本。这是一个用来返回单独一个任务的函数:

```python
from flask import abort

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = list(filter(lambda t: t['id'] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})
```

第二个函数有些意思。这里我们得到了 URL 中任务的 id，接着 Flask 把它转换成 函数中的 task_id 的参数。

我们用这个参数来搜索我们的任务数组。如果我们的数据库中不存在搜索的 id，我们将会返回一个类似 404 的错误，根据 HTTP 规范的意思是 “资源未找到”。

如果我们找到相应的任务，那么我们只需将它用 jsonify 打包成 JSON 格式并将其发送作为响应，就像我们以前那样处理整个任务集合。

调用 curl 请求的结果如下:

```bash
$ curl -i http://localhost:5000/todo/api/v1.0/tasks/2
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 151
Server: Werkzeug/0.8.3 Python/2.7.3
Date: Mon, 20 May 2013 05:21:50 GMT

{
  "task": {
    "description": "Need to find a good Python tutorial on the web",
    "done": false,
    "id": 2,
    "title": "Learn Python"
  }
}
$ curl -i http://localhost:5000/todo/api/v1.0/tasks/3
HTTP/1.0 404 NOT FOUND
Content-Type: text/html
Content-Length: 238
Server: Werkzeug/0.8.3 Python/2.7.3
Date: Mon, 20 May 2013 05:21:52 GMT

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.</p><p>If you     entered the URL manually please check your spelling and try again.</p>
```

当我们请求 id #2 的资源时候，我们获取到了，但是当我们请求 #3 的时候返回了 404 错误。有关错误奇怪的是返回的是 HTML 信息而不是 JSON，这是因为 Flask 按照默认方式生成 404 响应。由于这是一个 Web service 客户端希望我们总是以 JSON 格式回应，所以我们需要改善我们的 404 错误处理程序:

```python
from flask import make_response

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
```

我们会得到一个友好的错误提示:

```bash
$ curl -i http://localhost:5000/todo/api/v1.0/tasks/3
HTTP/1.0 404 NOT FOUND
Content-Type: application/json
Content-Length: 26
Server: Werkzeug/0.8.3 Python/2.7.3
Date: Mon, 20 May 2013 05:36:54 GMT

{
  "error": "Not found"
}
```

接下来就是 POST 方法，我们用来在我们的任务数据库中插入一个新的任务:

```python
from flask import request

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201
```

添加一个新的任务也是相当容易地。只有当请求以 JSON 格式形式，request.json 才会有请求的数据。如果没有数据，或者存在数据但是缺少 title 项，我们将会返回 400，这是表示请求无效。

接着我们会创建一个新的任务字典，使用最后一个任务的 id + 1 作为该任务的 id。我们允许 description 字段缺失，并且假设 done 字段设置成 False。

我们把新的任务添加到我们的任务数组中，并且把新添加的任务和状态 201 响应给客户端。

使用如下的 curl 命令来测试这个新的函数:

```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/api/v1.0/tasks
HTTP/1.0 201 Created
Content-Type: application/json
Content-Length: 104
Server: Werkzeug/0.8.3 Python/2.7.3
Date: Mon, 20 May 2013 05:56:21 GMT

{
  "task": {
    "description": "",
    "done": false,
    "id": 3,
    "title": "Read a book"
  }
}
```

注意：如果你在 Windows 上并且运行 Cygwin 版本的 curl，上面的命令不会有任何问题。然而，如果你使用原生的 curl，命令会有些不同:

```bash
curl -i -H "Content-Type: application/json" -X POST -d "{"""title""":"""Read a book"""}" http://localhost:5000/todo/api/v1.0/tasks
```

当然在完成这个请求后，我们可以得到任务的更新列表:

```bash
$ curl -i http://localhost:5000/todo/api/v1.0/tasks
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 423
Server: Werkzeug/0.8.3 Python/2.7.3
Date: Mon, 20 May 2013 05:57:44 GMT

{
  "tasks": [
    {
      "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
      "done": false,
      "id": 1,
      "title": "Buy groceries"
    },
    {
      "description": "Need to find a good Python tutorial on the web",
      "done": false,
      "id": 2,
      "title": "Learn Python"
    },
    {
      "description": "",
      "done": false,
      "id": 3,
      "title": "Read a book"
    }
  ]
}
```

剩下的两个函数如下所示:

```python
@app.route("/todo/api/v1.0/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = list(filter(lambda t: t["id"] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    # 在Python3中所有字符串都是Unicode字符串, 因此这里无需判断
    if "done" in request.json and type(request.json['done']) is not bool:
        abort(400)

    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = list(filter(lambda t: t["id"] == task_id, tasks))
    if len(task) == 0:
        abort(404)

    tasks.remove(task[0])
    return jsonify({"result": True})
```

delete_task 函数没有什么特别的。对于 update_task 函数，我们需要严格地检查输入的参数以防止可能的问题。我们需要确保在我们把它更新到数据库之前，任何客户端提供我们的是预期的格式。

更新任务 #2 的函数调用如下所示:

```bash
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000/todo/api/v1.0/tasks/2
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 170
Server: Werkzeug/0.8.3 Python/2.7.3
Date: Mon, 20 May 2013 07:10:16 GMT

{
  "task": [
    {
      "description": "Need to find a good Python tutorial on the web",
      "done": true,
      "id": 2,
      "title": "Learn Python"
    }
  ]
}
```

#### 优化web service接口

目前 API 的设计的问题就是迫使客户端在任务标识返回后去构造 URIs。这对于服务器是十分简单的，但是间接地迫使客户端知道这些 URIs 是如何构造的，这将会阻碍我们以后变更这些 URIs。

不直接返回任务的 ids，我们直接返回控制这些任务的完整的 URI，以便客户端可以随时使用这些 URIs。为此，我们可以写一个小的辅助函数生成一个 “公共” 版本任务发送到客户端:

```python
from flask import url_for

def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task.get("id", None), _external=True)
        else:
            new_task[field] = task[field]
    return new_task
```

这里所有做的事情就是从我们数据库中取出任务并且创建一个新的任务，这个任务的 id 字段被替换成通过 Flask 的 url_for 生成的 uri 字段。

当我们返回所有的任务列表的时候，在发送到客户端之前通过这个函数进行处理:

```python
@app.route("/todo/api/v1.0/tasks")
def get_tasks():
    return jsonify({"tasks": list(map(make_public_task, tasks))})
```

这里就是客户端获取任务列表的时候得到的数据:

```bash
$ curl -i http://localhost:5000/todo/api/v1.0/tasks
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 406
Server: Werkzeug/0.8.3 Python/2.7.3
Date: Mon, 20 May 2013 18:16:28 GMT

{
  "tasks": [
    {
      "title": "Buy groceries",
      "done": false,
      "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
      "uri": "http://localhost:5000/todo/api/v1.0/tasks/1"
    },
    {
      "title": "Learn Python",
      "done": false,
      "description": "Need to find a good Python tutorial on the web",
      "uri": "http://localhost:5000/todo/api/v1.0/tasks/2"
    }
  ]
}
```

我们将会把上述的方式应用到其它所有的函数上以确保客户端一直看到 URIs 而不是 ids。

#### 加强web service安全性

我们已经完成了我们 web service 的大部分功能，但是仍然有一个问题。我们的 web service 对任何人都是公开的，这并不是一个好主意。

我们有一个可以管理我们的待办事项完整的 web service，但在当前状态下的 web service 是开放给所有的客户端。 如果一个陌生人弄清我们的 API 是如何工作的，他或她可以编写一个客户端访问我们的 web service 并且毁坏我们的数据。

大部分初级的教程会忽略这个问题并且到此为止。在我看来这是一个很严重的问题，我必须指出。

确保我们的 web service 安全服务的最简单的方法是要求客户端提供一个用户名和密码。在常规的 web 应用程序会提供一个登录的表单用来认证，并且服务器会创建一个会话为登录的用户以后的操作使用，会话的 id 以 cookie 形式存储在客户端浏览器中。然而 REST 的规则之一就是 “无状态”， 因此我们必须要求客户端在每一次请求中提供认证的信息。

我们一直试着尽可能地坚持 HTTP 标准协议。既然我们需要实现认证我们需要在 HTTP 上下文中去完成，HTTP 协议提供了两种认证机制: [Basic 和 Digest](http://www.ietf.org/rfc/rfc2617.txt)。

有一个小的 Flask 扩展能够帮助我们，我们可以先安装 Flask-HTTPAuth:

```bash
$ flask/bin/pip install flask-httpauth
```

比方说，我们希望我们的 web service 只让访问用户名 xuefeng 和密码 python 的客户端访问。 我们可以设置一个基本的 HTTP 验证如下:

```python
@auth.get_password
def get_password(username):
    # 更好的方式是通过环境变量来获取, 而不是明文硬编码
    if username == "xuefeng":
        return "test_restful"
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
```

get_password 函数是一个回调函数，Flask-HTTPAuth 使用它来获取给定用户的密码。在一个更复杂的系统中，这个函数是需要检查一个用户数据库，但是在我们的例子中只有单一的用户因此没有必要。

error_handler 回调函数是用于给客户端发送未授权错误代码。像我们处理其它的错误代码，这里我们定制一个包含 JSON 数据格式而不是 HTML 的响应。

随着认证系统的建立，所剩下的就是把需要认证的函数添加 @auth.login_required 装饰器。例如:

```python
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    return jsonify({'tasks': tasks})
```

如果现在要尝试使用 curl 调用这个函数我们会得到:

```bash
$ curl -i http://localhost:5000/todo/api/v1.0/tasks
HTTP/1.0 401 UNAUTHORIZED
Content-Type: application/json
Content-Length: 36
WWW-Authenticate: Basic realm="Authentication Required"
Server: Werkzeug/0.8.3 Python/2.7.3
Date: Mon, 20 May 2013 06:41:14 GMT

{
  "error": "Unauthorized access"
}
```

为了能够调用这个函数我们必须发送我们的认证凭据:

```bash
$ curl -u xuefeng:test_restful -i http://localhost:5000/todo/api/v1.0/tasks
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 316
Server: Werkzeug/0.8.3 Python/2.7.3
Date: Mon, 20 May 2013 06:46:45 GMT

{
  "tasks": [
    {
      "title": "Buy groceries",
      "done": false,
      "description": "Milk, Cheese, Pizza, Fruit, Tylenol",
      "uri": "http://localhost:5000/todo/api/v1.0/tasks/1"
    },
    {
      "title": "Learn Python",
      "done": false,
      "description": "Need to find a good Python tutorial on the web",
      "uri": "http://localhost:5000/todo/api/v1.0/tasks/2"
    }
  ]
}
```

认证扩展给予我们很大的自由选择哪些函数需要保护，哪些函数需要公开。

为了确保登录信息的安全应该使用 HTTP 安全服务器(例如: [https://](https:)...)，这样客户端和服务器之间的通信都是加密的，以防止传输过程中第三方看到认证的凭据。

让人不舒服的是当请求收到一个 401 的错误，网页浏览都会跳出一个丑陋的登录框，即使请求是在后台发生的。因此如果我们要实现一个完美的 web 服务器的话，我们就需要禁止跳转到浏览器显示身份验证对话框，让我们的客户端应用程序自己处理登录。

一个简单的方式就是不返回 401 错误。403 错误是一个令人青睐的替代，403 错误表示 “禁止” 的错误:

```python
@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)
```

#### 更多可能的改进

我们编写的小型的 web service 还可以在不少的方面进行改进。

对于初学者来说，一个真正的 web service 需要一个真实的数据库进行支撑。我们现在使用的内存数据结构会有很多限制不应该被用于真正的应用。

另外一个可以提高的领域就是处理多用户。如果系统支持多用户的话，不同的客户端可以发送不同的认证凭证获取相应用户的任务列表。在这样一个系统中的话，我们需要第二个资源就是用户。在用户资源上的 POST 的请求代表注册换一个新用户。一个 GET 请求表示客户端获取一个用户的信息。一个 PUT 请求表示更新用户信息，比如可能是更新邮箱地址。一个 DELETE 请求表示删除用户账号。

GET 检索任务列表请求可以在几个方面进行扩展。首先可以携带一个可选的页的参数，以便客户端请求任务的一部分。另外，这种扩展更加有用：允许按照一定的标准筛选。比如，用户只想要看到完成的任务，或者只想看到任务的标题以 A 字母开头。所有的这些都可以作为 URL 的一个参数项。

### Flask扩展

Flask的设计考虑了可扩展性，故而没有提供一些重要的功能，例如数据库和用户身份验证，所以开发者可以自由选择最适合应用的包，或者按需求自行开发。

社区成员开发了大量不同用途的Flask扩展，如果这还不能满足需求，任何Python标准包或代码库都可以使用。

就我目前觉得，掌握Flask核心（Flask、Jinja2、CLI），而后掌握Flask-WTF、WTForms、Flask-SQLAlchemy、Flask-Login分别更好的更安全的完成Web表单，数据库，用户登录的开发，像Flask-Bootstrap、Flask-Moment以及其他的扩展，在实际开发需要用到时查阅文档即可，甚至有时候就别用那些扩展了，自己来写。

#### Flask-WTF

**Flask-WTF** 提供了简单地 [WTForms](http://wtforms.simplecodes.com/docs/) 的集成。

**1.特性：**

- 集成 wtforms。
- 带有 csrf 令牌的安全表单。
- 全局的 csrf 保护。
- 支持验证码（Recaptcha）。
- 支持 Flask-Uploads 的文件上传。
- 国际化集成。

**2.创建表单：**

```python
from flask-wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired	

class MyForm(Form):
    text = TextField("text", validators=[DataRequired(), ])
```

注解：从 0.9.0 版本开始，Flask-WTF 不再从 WTforms 中导入任何东西，你需要从 WTForms 导入字段。

此外，CSRF 令牌的隐藏字段是自动创建的。你可以在模板中这样渲染它:

```jinja2
<form method="POST" action="/">
	{{ form.csrf_token }}
	{{ form.text.label }} {{ form.text(size=20)}}
	<input type="submit" value="Go">
</form>
```

尽管如此，为了创建有效的 XHTML/HTML， `Form` 类有一个 `hidden_tag` 方法， 它在一个隐藏的 DIV 标签中渲染任何隐藏的字段，包括 CSRF 字段:

```jinja2
<form method="POST" action="/">
    {{ form.hidden_tag() }}
    {{ form.text.label }} {{ form.text(size=20) }}
    <input type="submit" value="Go">
</form>
```

**3.验证表单：**

在视图函数中验证请求:

```python
@app.route("/submit", methods=["GET", "POST"])
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect("/success")
    return render_template("submit.heml", form=form)
```

**4.文件上传：**

Flask-WTF 提供了 [`FileField`](https://docs.jinkan.org/docs/flask-wtf/api.html#flask_wtf.file.FileField) 类来处理文件上传，它在表单提交后， 自动从 `flask.request.files` 抽取数据。 `FileField`` 的 `data` 属性是一个 Werkzeug FileStorage 实例。例如:

```python
from werkzeug import secure_filename
from flask_wtf.files import FileField

class PhotoForm(Form):
    photo = FileField("Your photo")
    
@app.route("/upload", methods=["GET", "POST"])
def upload():
	form = PhotoForm()
	if form.validate_on_submit():
		filename = secure_filename(form.photo.data.filename)
	else:
		filename = None
	return render_template("upload.html", form=form, filename=filename)
```

注解：请记得设置 HTML 表单的 `enctype` 为 `multipart/form-data` ， 即:

```html
<form action="/upload/" method="POST" enctype="multipart/form-data">
	...
</form>
```

此外，Flask-WTF 支持文件上传的验证。提供了 [`FileRequired`](https://docs.jinkan.org/docs/flask-wtf/api.html#flask_wtf.file.FileRequired) 和 [`FileAllowed`](https://docs.jinkan.org/docs/flask-wtf/api.html#flask_wtf.file.FileAllowed) 。

[`FileAllowed`](https://docs.jinkan.org/docs/flask-wtf/api.html#flask_wtf.file.FileAllowed) 可与 Flask-Uploads 协同工作，例如:

```python
from flask.ext.uploads import UploadSet, IMAGES
from flask_wtf import Form
from flask_wtf.file import FileField, FileAllowed, FileRequired

images = UploadSet('images', IMAGES)

class UploadForm(Form):
    upload = FileField('image', validators=[
        FileRequired(),
        FileAllowed(images, 'Images only!')
    ])
```

它也可以在没有 Flask-Uploads 的情况下工作。你需要向 [`FileAllowed`](https://docs.jinkan.org/docs/flask-wtf/api.html#flask_wtf.file.FileAllowed) 传递扩展名:

```python
class UploadForm(Form):
    upload = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
```

**5.Recaptcha：**

Flask-WTF 也通过 `RecaptchaField` 提供了对 Recaptcha 的支持:

```python
from flask_wtf import Form, RecaptchaField
from wtforms import TextField

class SignupForm(Form):
    username = TextField('Username')
    recaptcha = RecaptchaField()
```

这伴随着诸多配置，你需要逐一实现他们。

| RECAPTCHA_USE_SSL     | 允许/禁用 Recaptcha 使用 SSL。默认是 `False`。               |
| --------------------- | ------------------------------------------------------------ |
| RECAPTCHA_PUBLIC_KEY  | **必需** 公钥。                                              |
| RECAPTCHA_PRIVATE_KEY | **必需** 私钥。                                              |
| RECAPTCHA_OPTIONS     | **可选** 配置选项的字典。 https://www.google.com/recaptcha/admin/create |

对于应用测试时，如果 `app.testing` 为 `True` ，考虑到方便测试， Recaptcha 字段总是有效的。在模板中很容易添加 Recaptcha 字段:

```jinja2
<form action="/" method="post">
    {{ form.username }}
    {{ form.recaptcha }}
</form>
```

示例： [recaptcha@github](https://github.com/lepture/flask-wtf/tree/master/examples/recaptcha).

**6.CSRF 保护：**

Flask-WTF 表单保护你免受 CSRF 威胁，你不需要有任何担心。尽管如此，如果你有不包含表单的视图，那么它们仍需要额外的保护。

例如，由 AJAX 发送的 POST 请求，并没有通过表单。在 0.9.0 之前版本，你无法获得 CSRF 令牌。这就是为什么我们编写了 CSRF 模块。

要对所有视图函数启用 CSRF 保护，你需要启用 [`CSRFProtect`](https://docs.jinkan.org/docs/flask-wtf/api.html#flask_wtf.csrf.CsrfProtect) 模块:

```python
from flask_wtf.csrf import CSRFProtect

CSRFProtect(app)
```

与任何其它的 Flask 扩展一样，你可以惰性加载它:

```python
from flask_wtf.csrf import CsrfProtect

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    csrf.init_app(app)
```

注解：你需要为 CSRF 指定一个密钥。通常，这与你的 Flask 应用 `SECRET_KEY` 一致。

如果模板中有表单，你不需要做任何事。与之前一样:

```jinja2
<form method="post" action="/">
    {{ form.csrf_token }}
    ...
</form>
```

但如果模板中没有表单，你仍需要 CSRF 令牌:

```jinja2
<form method="post" action="/">
    <input type="hidden" name="csrf_token" value="{{ csrf_token() }}" />
</form>
```

无论何时未通过 CSRF 验证，都会返回 400 响应。你可以自定义这个错误响应:

```python
@csrf.error_handler
def csrf_error(reason):
    return render_template('csrf_error.html', reason=reason), 400
```

我们强烈建议你对所有视图启用 CSRF 保护。但也提供了将某些视图函数除外的途径:

```python
@csrf.exempt
@app.route('/foo', methods=('GET', 'POST'))
def my_handler():
    # ...
    return 'ok'
```

通过 AJAX 发送 POST 请求并不需要表单。这个特性在 0.9.0 之后可用。

假设你已经使用了 `CsrfProtect(app)` ，你可以通过 `{{ csrf_token() }}` 获取 CSRF 令牌。这个方法在每个模板中都可以使用，你并不需要担心在没有表单时如何渲染 CSRF 令牌字段。

我们推荐的方式是在 `<meta>` 标签中渲染 CSRF 令牌:

```jinja2
<meta name="csrf-token" content="{{ csrf_token() }}">
```

在 `<script>` 标签中渲染同样可行:

```jinja2
<script type="text/javascript">
    var csrftoken = "{{ csrf_token() }}"
</script>
```

下面的例子采用了 `<meta>` 的方式， `<script>` 会更简单，你无须担心没有对应的例子。

无论何时你发送 AJAX POST 请求，为其添加 `X-CSRFToken` 标头:

```jinja2
var csrftoken = $('meta[name=csrf-token]').attr('content')

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken)
        }
    }
})
```

#### Flask-Login

Flask-Login 为 Flask 提供了用户会话管理。它处理了日常的登入，登出并且长时间记住用户的会话。

它会:

- 在会话中存储当前活跃的用户 ID，让你能够自由地登入和登出。
- 让你限制登入(或者登出)用户可以访问的视图。
- 处理让人棘手的 “记住我” 功能。
- 帮助你保护用户会话免遭 cookie 被盗的牵连。
- 可以与以后可能使用的 Flask-Principal 或其它认证扩展集成。

但是，它不会:

- 限制你使用特定的数据库或其它存储方法。如何加载用户完全由你决定。
- 限制你使用用户名和密码，OpenIDs，或者其它的认证方法。
- 处理超越 “登入或者登出” 之外的权限。
- 处理用户注册或者账号恢复。

**1.配置你的应用：**

对一个使用 Flask-Login 的应用最重要的一部分就是 [`LoginManager`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.LoginManager) 类。你应该在你的代码的某处为应用创建一个，像这样:

```python
from flask_login import LoginManager

login_manager = LoginManager()
```

登录管理(login manager)包含了让你的应用和 Flask-Login 协同工作的代码，比如怎样从一个 ID 加载用户，当用户需要登录的时候跳转到哪里等等。

一旦实际的应用对象创建后，你能够这样配置它来实现登录:

```python
login_manager(app)
```

亦可以使用惰性加载：

```python
login_manager.init_app(app)
```

**2.它是如何工作：**

你必须提供一个 [`user_loader`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.LoginManager.user_loader) 回调。这个回调用于从会话中存储的用户 ID 重新加载用户对象。它应该接受一个用户的 [`unicode`](http://docs.python.org/library/functions.html#unicode) ID 作为参数，并且返回相应的用户对象。比如:

```python
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
```

如果 ID 无效的话，它应该返回 [`None`](http://docs.python.org/library/constants.html#None) (**而不是抛出异常**)。(在这种情况下，ID 会被手动从会话中移除且处理会继续)

**3.你的用户类：**

你用来表示用户的类需要实现这些属性和方法:

```python
is_authenticated
```

当用户通过验证时，也即提供有效证明时返回 [`True`](http://docs.python.org/library/constants.html#True) 。（只有通过验证的用户会满足 [`login_required`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.login_required) 的条件。）

```python
is_active
```

如果这是一个活动用户且通过验证，账户也已激活，未被停用，也不符合任何你 的应用拒绝一个账号的条件，返回 [`True`](http://docs.python.org/library/constants.html#True) 。不活动的账号可能不会登入（当然， 是在没被强制的情况下）。

```python
is_anonymous
```

如果是一个匿名用户，返回 [`True`](http://docs.python.org/library/constants.html#True) 。（真实用户应返回 [`False`](http://docs.python.org/library/constants.html#False) 。）

```python
get_id()
```

返回一个能唯一识别用户的，并能用于从 [`user_loader`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.LoginManager.user_loader) 回调中加载用户的 [`unicode`](http://docs.python.org/library/functions.html#unicode) 。注意着 **必须** 是一个 [`unicode`](http://docs.python.org/library/functions.html#unicode) —— 如果 ID 原本是 一个 [`int`](http://docs.python.org/library/functions.html#int) 或其它类型，你需要把它转换为 [`unicode`](http://docs.python.org/library/functions.html#unicode) 。

要简便地实现用户类，你可以从 [`UserMixin`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.UserMixin) 继承，它提供了对所有这些方法的默认 实现。（虽然这不是必须的。）

**4.Login示例：**

一旦用户通过验证，你可以使用 [`login_user`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.login_user) 函数让用户登录。例如:

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # next_is_valid should check if the user has valid
        # permission to access the `next` url
        if not next_is_valid(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)
```

*警告:* 你必须验证 [`next`](http://docs.python.org/library/functions.html#next) 参数的值。如果不验证的话，你的应用将会受到重定向的攻击。

就这么简单。你可用使用 [`current_user`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.current_user) 代理来访问登录的用户，在每一个模板中都可以使用 [`current_user`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.current_user):

```jinja2
{% if current_user.is_authenticated() %}
  Hi {{ current_user.name }}!
{% endif %}
```

需要用户登入 的视图可以用 [`login_required`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.login_required) 装饰器来装饰:

```python
@app.route("/settings")
@login_required
def settings():
    pass
```

当用户要登出时:

```python
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(somewhere)
```

他们会被登出，且他们会话产生的任何 cookie 都会被清理干净。

**5.定制登入过程：**

默认情况下，当未登录的用户尝试访问一个 [`login_required`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.login_required) 装饰的视图，Flask-Login 会闪现一条消息并且重定向到登录视图。(如果未设置登录视图，它将会以 401 错误退出。)

登录视图的名称可以设置成 [`LoginManager.login_view`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.LoginManager.login_view)。例如:

```python
login_manager.login_view = "auth.login"
```

默认的闪现消息是 `Please log in to access this page.`。要自定义该信息，请设置 [`LoginManager.login_message`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.LoginManager.login_message):

```python
login_manager.login_message = "Please log in to access this page."
```

要自定义消息分类的话，请设置 `LoginManager.login_message_category`:

```python
login_manager.login_message_category = "info"
```

当重定向到登入视图，它的请求字符串中会有一个 `next` 变量，其值为用户之前访问的页面。

如果你想要进一步自定义登入过程，请使用 [`LoginManager.unauthorized_handler`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.LoginManager.unauthorized_handler) 装饰函数:

```python
@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return a_response
```

**6.使用授权头(Authorization header)登录：**

有时你想要不使用 cookies 情况下登录用户，比如使用 HTTP 头或者一个作为查询参数的 api 密钥。这种情况下，你应该使用 `request_loader` 回调。这个回调和 [`user_loader`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.LoginManager.user_loader) 回调作用一样，但是 [`user_loader`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.LoginManager.user_loader) 回调只接受 Flask 请求而不是一个 user_id。

例如，为了同时支持一个 url 参数和使用 `Authorization` 头的基本用户认证的登录:

```python
@login_manager.request_loader
def load_user_from_request(request):

    # first, try to login using the api_key url arg
    api_key = request.args.get('api_key')
    if api_key:
        user = User.query.filter_by(api_key=api_key).first()
        if user:
            return user

    # next, try to login using Basic Auth
    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Basic ', '', 1)
        try:
            api_key = base64.b64decode(api_key)
        except TypeError:
            pass
        user = User.query.filter_by(api_key=api_key).first()
        if user:
            return user

    # finally, return None if both methods did not login the user
    return None
```

**7.匿名用户：**

默认情况下，当一个用户没有真正地登录，[`current_user`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.current_user) 被设置成一个 `AnonymousUserMixin` 对象。它由如下的属性和方法:

- `is_active` 和 `is_authenticated` 的值为 [`False`](http://docs.python.org/library/constants.html#False)
- `is_anonymous` 的值为 [`True`](http://docs.python.org/library/constants.html#True)
- `get_id()` 返回 [`None`](http://docs.python.org/library/constants.html#None)

如果需要为匿名用户定制一些需求(比如，需要一个权限域)，你可以向 [`LoginManager`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.LoginManager) 提供一个创建匿名用户的回调（类或工厂函数）:

```python
login_manager.anonymous_user = MyAnonymousUser
```

**8.记住我：**

“记住我”的功能很难实现。但是，Flask-Login 几乎透明地实现它 - 只要把 `remember=True` 传递给 [`login_user`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.login_user)。一个 cookie 将会存储在用户计算机中，如果用户会话中没有用户 ID 的话，Flask-Login 会自动地从 cookie 中恢复用户 ID。cookie 是防纂改的，因此如果用户纂改过它(比如，使用其它的一些东西来代替用户的 ID)，它就会被拒绝，就像不存在。

该层功能是被自动实现的。但你能（且应该，如果你的应用处理任何敏感的数据）提供 额外基础工作来增强你记住的 cookie 的安全性。

**9.可选令牌：**

使用用户 ID 作为记住的令牌值不一定是安全的。更安全的方法是使用用户名和密码联合的 hash 值，或类似的东西。要添加一个额外的令牌，向你的用户对象添加一个方法：

```python
get_auth_token()
```

返回用户的认证令牌（返回为 [`unicode`](http://docs.python.org/library/functions.html#unicode) ）。这个认证令牌应能唯一识别用户，且不易通过用户的公开信息，如 UID 和名称来猜测出——同样也不应暴露这些信息。

相应地，你应该在 [`LoginManager`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.LoginManager) 上设置一个 [`token_loader`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.LoginManager.token_loader) 函数， 它接受令牌（存储在 cookie 中）作为参数并返回合适的 User 对象。

[`make_secure_token`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.make_secure_token) 函数用于便利创建认证令牌。它会连接所有的参数，然后用应用的密钥来 HMAC 它确保最大的密码学安全。（如果你永久地在数据库中存储用户令牌，那么你会希望向令牌中添加随机数据来阻碍猜测。）

如果你的应用使用密码来验证用户，在认证令牌中包含密码（或你应使用的加盐值的密码 hash ）能确保若用户更改密码，他们的旧认证令牌会失效。

**10.新鲜的“登录(Fresh Logins)：**

当用户登入，他们的会话被标记成“新鲜的”，就是说在这个会话中用户实际上登录过。当会话销毁用户使用“记住我”的 cookie 重新登入，会话被标记成“非新鲜的”。[`login_required`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.login_required) 并不在意它们之间的不同，这适用于大部分页面。然而，更改某人 的个人信息这样的敏感操作应需要一个“新鲜的”的登入。（像修改密码这样的操作总是需要 密码，无论是否重登入。）

[`fresh_login_required`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.fresh_login_required)，除了验证用户登录，也将确保他们的登录是“新鲜的”。如果不是“新鲜的”，它会把用户送到可以重输入验证条件的页面。你可以定制 [`fresh_login_required`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.fresh_login_required) 就像定制 [`login_required`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.login_required) 那样，通过设置 [`LoginManager.refresh_view`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.LoginManager.refresh_view)，[`needs_refresh_message`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.LoginManager.needs_refresh_message)，和 `needs_refresh_message_category`:

```python
login_manager.refresh_view = "accounts.reauthenticate"
login_manager.needs_refresh_message = (
    u"To protect your account, please reauthenticate to access this page."
)
login_manager.needs_refresh_message_category = "info"
```

或者提供自己的回调来处理“非新鲜的”刷新:

```python
@login_manager.needs_refresh_handler
def refresh():
    # do stuff
    return a_response
```

**11.会话保护：**

当上述特性保护“记住我”令牌免遭 cookie 窃取时，会话 cookie 仍然是脆弱的。 Flask-Login 包含了会话保护来帮助阻止用户会话被盗用。

你可以在 [`LoginManager`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.LoginManager) 上和应用配置中配置会话保护。如果它被启用，它可以在 `basic` 或 `strong` 两种模式中运行。要在 [`LoginManager`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.LoginManager) 上设置它，设置 `session_protection` 属性为 `"basic"` 或 `"strong"`:

```python
login_manager.session_protection = "strong"
```

或者，禁用它:

```python
login_manager.session_protection = None
```

默认，它被激活为 `"basic"` 模式。它可以在应用配置中设定 `SESSION_PROTECTION` 为 [`None`](http://docs.python.org/library/constants.html#None) 、 `"basic"` 或 `"strong"` 来禁用。

当启用了会话保护，每个请求，它生成一个用户电脑的标识（基本上是 IP 地址和 User Agent 的 MD5 hash 值）。如果会话不包含相关的标识，则存储生成的。如果存在标识，则匹配生成的，之后请求可用。

在 `basic` 模式下或会话是永久的，如果该标识未匹配，会话会简单地被标记为非活 跃的，且任何需要活跃登入的东西会强制用户重新验证。（当然，你必须已经使用了活跃登入机制才能奏效。）

在 `strong` 模式下的非永久会话，如果该标识未匹配，整个会话（记住的令牌如果存在，则同样）被删除。

**12.本地化：**

默认情况下，当用户需要登录，[`LoginManager`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.LoginManager) 使用 `flash` 来显示信息。这些信息都是英文的。如果你需要本地化，设置 [`LoginManager`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-login.html#flask.ext.login.LoginManager) 的 `localize_callback` 属性为一个函数，该函数在消息被发送到 `flash` 的时候被调用，比如，`gettext`。

#### Flask-RESTful

**Flask-RESTful** 是一个 Flask 扩展，它添加了快速构建 REST APIs 的支持。它当然也是一个能够跟你现有的ORM/库协同工作的轻量级的扩展。Flask-RESTful 鼓励以最小设置的最佳实践。如果你熟悉 Flask 的话，Flask-RESTful 应该很容易上手。

**1.一个最小的 API：**

一个最小的 Flask-RESTful API 像这样:

```python
from flask import Flask
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)

class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
```

把上述代码保存为 api.py 并且在你的 Python 解释器中运行它。需要注意地是我们已经启用了 [Flask 调试](http://flask.pocoo.org/docs/quickstart/#debug-mode) 模式，这种模式提供了代码的重载以及更好的错误信息。调试模式绝不能在生产环境下使用。

```shell
$ python api.py
 * Running on http://127.0.0.1:5000/
```

现在打开一个新的命令行窗口使用 curl 测试你的 API:

```shell
$ curl http://127.0.0.1:5000/
{"hello": "world"}
```

**2.资源丰富的路由(Resourceful Routing)：**

Flask-RESTful 提供的最主要的基础就是资源(resources)。资源(Resources)是构建在 [Flask 可拔插视图](http://flask.pocoo.org/docs/views/) 之上，只要在你的资源(resource)上定义方法就能够容易地访问多个 HTTP 方法。一个待办事项应用程序的基本的 CRUD 资源看起来像这样:

```python
from flask import Flask, request
from flask.ext.restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
```

你可以尝试这样:

```shell
$ curl http://localhost:5000/todo1 -d "data=Remember the milk" -X PUT
{"todo1": "Remember the milk"}
$ curl http://localhost:5000/todo1
{"todo1": "Remember the milk"}
$ curl http://localhost:5000/todo2 -d "data=Change my brakepads" -X PUT
{"todo2": "Change my brakepads"}
$ curl http://localhost:5000/todo2
{"todo2": "Change my brakepads"}
```

或者如果你安装了 requests 库的话，可以从 python shell 中运行:

```shell
>>> from requests import put, get
>>> put('http://localhost:5000/todo1', data={'data': 'Remember the milk'}).json()
{u'todo1': u'Remember the milk'}
>>> get('http://localhost:5000/todo1').json()
{u'todo1': u'Remember the milk'}
>>> put('http://localhost:5000/todo2', data={'data': 'Change my brakepads'}).json()
{u'todo2': u'Change my brakepads'}
>>> get('http://localhost:5000/todo2').json()
{u'todo2': u'Change my brakepads'}
```

Flask-RESTful 支持视图方法多种类型的返回值。同 Flask 一样，你可以返回任一迭代器，它将会被转换成一个包含原始 Flask 响应对象的响应。Flask-RESTful 也支持使用多个返回值来设置响应代码和响应头，如下所示:

```python
class Todo1(Resource):
    def get(self):
        # Default to 200 OK
        return {'task': 'Hello world'}

class Todo2(Resource):
    def get(self):
        # Set the response code to 201
        return {'task': 'Hello world'}, 201

class Todo3(Resource):
    def get(self):
        # Set the response code to 201 and return custom headers
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}
```

**2.端点(Endpoints)：**

很多时候在一个 API 中，你的资源可以通过多个 URLs 访问。你可以把多个 URLs 传给 Api 对象的 [`Api.add_resource()`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/api.html#flask.ext.restful.Api.add_resource) 方法。每一个 URL 都能访问到你的 [`Resource`](https://wizardforcel.gitbooks.io/flask-extension-docs/content/api.html#flask.ext.restful.Resource)

```python
api.add_resource(HelloWorld, '/', '/hello')
```

你也可以为你的资源方法指定 endpoint 参数。

```python
api.add_resource(Todo,
    '/todo/<int:todo_id>', endpoint='todo_ep')
```

**3.参数解析：**

尽管 Flask 能够简单地访问请求数据(比如查询字符串或者 POST 表单编码的数据)，验证表单数据仍然很痛苦。Flask-RESTful 内置了支持验证请求数据，它使用了一个类似 [argparse](http://docs.python.org/dev/library/argparse.html) 的库。

```python
from flask.ext.restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('rate', type=int, help='Rate to charge for this resource')
args = parser.parse_args()
```

需要注意地是与 argparse 模块不同，`reqparse.RequestParser.parse_args()` 返回一个 Python 字典而不是一个自定义的数据结构。

使用 [`reqparse`](http://www.pythondoc.com/Flask-RESTful/api.html#module-reqparse) 模块同样可以自由地提供聪明的错误信息。如果参数没有通过验证，Flask-RESTful 将会以一个 400 错误请求以及高亮的错误信息回应。

```shell
$ curl -d 'rate=foo' http://127.0.0.1:5000/
{'status': 400, 'message': 'foo cannot be converted to int'}
```

**4.数据格式化：**

默认情况下，在你的返回迭代中所有字段将会原样呈现。尽管当你刚刚处理 Python 数据结构的时候，觉得这是一个伟大的工作，但是当实际处理它们的时候，会觉得十分沮丧和枯燥。为了解决这个问题，Flask-RESTful 提供了 `fields` 模块和 [`marshal_with()`](http://www.pythondoc.com/Flask-RESTful/api.html#flask.ext.restful.marshal_with) 装饰器。类似 Django ORM 和 WTForm，你可以使用 fields 模块来在你的响应中格式化结构。

```python
from collections import OrderedDict
from flask.ext.restful import fields, marshal_with

resource_fields = {
    'task':   fields.String,
    'uri':    fields.Url('todo_ep')
}

class TodoDao(object):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task

        # This field will not be sent in the response
        self.status = 'active'

class Todo(Resource):
    @marshal_with(resource_fields)
    def get(self, **kwargs):
        return TodoDao(todo_id='my_todo', task='Remember the milk')
```

上面的例子接受一个 python 对象并准备将其序列化。[`marshal_with()`](http://www.pythondoc.com/Flask-RESTful/api.html#flask.ext.restful.marshal_with) 装饰器将会应用到由 `resource_fields` 描述的转换。从对象中提取的唯一字段是 `task`。`fields.Url` 域是一个特殊的域，它接受端点（endpoint）名称作为参数并且在响应中为该端点生成一个 URL。许多你需要的字段类型都已经包含在内。请参阅 `fields` 指南获取一个完整的列表。

**5.完整的例子：**

在 api.py 中保存这个例子：

```python
from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


# Todo
# show a single todo item and lets you delete them
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
```

用法示例：

```shell
$ python api.py
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader
```

获取列表：

```shell
$ curl http://localhost:5000/todos
{"todo1": {"task": "build an API"}, "todo3": {"task": "profit!"}, "todo2": {"task": "?????"}}
```

获取一个单独的任务：

```shell
$ curl http://localhost:5000/todos/todo3
{"task": "profit!"}
```

删除一个任务

```shell
$ curl http://localhost:5000/todos/todo2 -X DELETE -v

> DELETE /todos/todo2 HTTP/1.1
> User-Agent: curl/7.19.7 (universal-apple-darwin10.0) libcurl/7.19.7 OpenSSL/0.9.8l zlib/1.2.3
> Host: localhost:5000
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 204 NO CONTENT
< Content-Type: application/json
< Content-Length: 0
< Server: Werkzeug/0.8.3 Python/2.7.2
< Date: Mon, 01 Oct 2012 22:10:32 GMT
```

增加一个新的任务

```shell
$ curl http://localhost:5000/todos -d "task=something new" -X POST -v

> POST /todos HTTP/1.1
> User-Agent: curl/7.19.7 (universal-apple-darwin10.0) libcurl/7.19.7 OpenSSL/0.9.8l zlib/1.2.3
> Host: localhost:5000
> Accept: */*
> Content-Length: 18
> Content-Type: application/x-www-form-urlencoded
>
* HTTP 1.0, assume close after body
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: 25
< Server: Werkzeug/0.8.3 Python/2.7.2
< Date: Mon, 01 Oct 2012 22:12:58 GMT
<
* Closing connection #0
{"task": "something new"}
```

更新一个任务

```shell
$ curl http://localhost:5000/todos/todo3 -d "task=something different" -X PUT -v

> PUT /todos/todo3 HTTP/1.1
> Host: localhost:5000
> Accept: */*
> Content-Length: 20
> Content-Type: application/x-www-form-urlencoded
>
* HTTP 1.0, assume close after body
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: 27
< Server: Werkzeug/0.8.3 Python/2.7.3
< Date: Mon, 01 Oct 2012 22:13:00 GMT
<
* Closing connection #0
{"task": "something different"}
```