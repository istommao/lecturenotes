title: python wsgi
speaker: silence
url: https://github.com/ksky521/nodePPT
transition: cards
files: /js/demo.js,/css/demo.css

[slide]

# wsgi
## 演讲者：silence

[slide]

# Web Server Gateway Interface {:&.flexbox.vleft}

## 定义

> Web服务器网关接口（Python Web Server Gateway Interface，缩写为WSGI）是为Python语言定义的Web服务器和Web应用程序或框架之间的一种简单而通用的接口。
> 自从WSGI被开发出来以后，许多其它语言中也出现了类似接口

## 注意

> WSGI不是服务器，不是API，不是Python模块，更不是什么框架，而是一种服务器和客户端交互的接口规范！

[slide]

# CGI {:&.flexbox.vleft}

> CGI是外部应用程序（CGI程序）与WEB服务器之间的接口标准

## 处理流程

- 通过Internet把用户请求送到web服务器。
- web服务器接收用户请求并交给CGI程序处理。
- CGI程序把处理结果传送给web服务器。
- web服务器把结果送回到用户。


[slide]

# CGI {:&.flexbox.vleft}

## 优点

- 动态网页, 加载数据、数据运算等

## 缺点

- 每次请求都要重新 启动进程、处理请求、结束进程，服务器性能

[slide]

# FastCGI {:&.flexbox.vleft}

- 减少了 Server 与 CGI 应用之间的交互开销

初始化时启动一个 FastCGI Server 常驻内存，处理请求

[slide]

![](/image/wsgi2.jpg)

## 回到 wsgi

> WSGI 是 Web 服务器和 Web 应用程序之间的一种简单而通用的接口，最初是为 Python 量身定做。

[slide]


![](/image/wsgi.png)

## wsgi

```python
def application(environ, start_response):
    data = b"Hello WSGI!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return [data]
```

[slide]

![](/image/wsgi-flow.png)


# server app 分别有哪些  {:&.flexbox.vleft}

## server/gateway
- gunicorn
- uWSGI
- mod_wsgi

## app/framework

- flask
- django
- Tornado
- Pyramid
- web.py
- ...

[slide]

# gunicorn 示例  {:&.flexbox.vleft}

## 安装

```python
pip install gunicorn
```

```python
# app.py
def application(environ, start_response):
    data = b'Hello WSGI!\n'
    headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response("200 OK", headers)

    return iter([data])
```

```bash
gunicorn -w 4 app:application
```

[slide]


## 相关链接

https://www.biaodianfu.com/cgi-fastcgi-wsgi.html
https://my.oschina.net/u/90679/blog/106725

[slide]

# 谢谢

Github：https://github.com/istommao/lecturenotes
