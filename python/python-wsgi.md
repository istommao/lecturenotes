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


![](/image/wsgi2.jpg)

[slide]

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

