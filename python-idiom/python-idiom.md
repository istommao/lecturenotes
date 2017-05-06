title: python idiom
speaker: silence
url: https://github.com/ksky521/nodePPT
transition: vertical3d


[slide style="background-color:#2C3F51"]

# python idiom
## Author：silence


[slide style="background-color:#2C3F51"]

# 概览 {:&.flexbox.vleft}

- 检查变量是否等于常量
- 编写函数的几个原则
- 列表推导式
- 善用装饰器
- 数据交换值的时候不推荐使用中间变量
- 连接字符串应优先使用 join 而不是 +
- 元素是否存在字典中
- 迭代的时候带上序号
- 使用 with 读取文件
- 使用pylint做代码质量检测


[slide style="background-color:#2C3F51"]

## 编写函数的几个原则

- 原则 1：函数设计要尽量短小，嵌套层次不宜过深。最好能控制在 3 层以内。
- 原则 2：函数申明应该做到合理、简单、易于使用。参数个数不宜太多。
- 原则 3：函数参数设计应该考虑向下兼容。比如相同功能的函数不同版本的实现，唯一不同的是在更高级的版本中添加了参数导致程序中函数调用的接口发生了改变。这并不是最佳设计，更好的方法是通过加入默认参数来避免这种退化，做到向下兼容。
- 原则 4：一个函数只做一件事，尽量保证函数语句粒度的一致性。
- 原则 5：不要在函数中定义可变对象作为默认值
- 原则 6：使用异常替换返回错误
- 原则 7：保证通过单元测试

[slide style="background-color:#2C3F51"]

# 迭代的时候带上序号 {:&.flexbox.vleft}

## Bad

```python
index = 0
for item in [1, 2, 3, 4]:
    print(index, item)
    index += 1
```

## Good

```python
for index, item in enumerate([1, 2, 3, 4]):
    print(index, item)
```



[slide style="background-color:#2C3F51"]

# 元素是否存在字典中 {:&.flexbox.vleft}

## Bad

```python
datadict = {'name': 'tommao', 'age': 25}
'name' in datadict.keys()
```

## Good

```python
datadict = {'name': 'tommao', 'age': 25}
'name' in datadict
```

## 比对
![](/_image/2017-03-22-20-46-22.jpg)


[slide style="background-color:#2C3F51"]

# Python函数参数默认值的陷阱 {:&.flexbox.vleft}

## Bad

```
def func(lst=[]):
    lst.append(1)
    print(lst)
```

## Good
```
def func(lst=None):
    if lst is None:
        lst = []
    lst.append(1)
    print(lst)
```


![](/_image/2017-03-22-21-02-50.jpg)


[Python函数参数默认值的陷阱和原理深究](http://cenalulu.github.io/python/default-mutable-arguments/)

[slide style="background-color:#2C3F51"]

# 连接字符串应优先使用 join 而不是 + {:&.flexbox.vleft}

```python
strlist = ['a', 'b', 'c']
strs = ''.join(strlist)
```


[slide style="background-color:#2C3F51"]
# 使用级联比较 a < b < c {:&.flexbox.vleft}

## Bad

```python
a, b, c = 1, 2, 3
if a < b and b < c:
    pass
```

## Good

```python
a, b, c = 1, 2, 3
if a < b < c:
    pass
```


[slide style="background-color:#2C3F51"]

# 用**而不是pow {:&.flexbox.vleft}


![](/_image/2017-03-22-21-16-44.jpg)



[slide style="background-color:#2C3F51"]

# 检查变量是否等于常量 {:&.flexbox.vleft}

## Bad


```python
if attr == True:
    print('True!')

if attr == None:
    print('attr is None!')
```

## Good

```python
# Just check the value
if attr:
    print('attr is truthy!')

# or check for the opposite
if not attr:
    print('attr is falsey!')

# or, since None is considered false, explicitly check for it
if attr is None:
    print('attr is None!')

```


[slide style="background-color:#2C3F51"]

# 不借助中间变量交换两个变量的值 {:&.flexbox.vleft}

## Bad

```python
a = 5
b = 10
temp = a
a = b
b = a
```

## Good

```python
a = 5
b = 10
a, b = b, a
```


[slide style="background-color:#2C3F51"]


# 列表推导式 {:&.flexbox.vleft}

## Bad

```python
result = []
for i in range(1, 1000):
    if i % 2 == 0:
        result.append(i)
```

## Good

```python
result = [i for i in range(1, 1000) if i % 2 == 0]
```


[slide style="background-color:#2C3F51"]

# 使用 with 读取文件 {:&.flexbox.vleft}

## Bad

```python
f = open('file.txt')
a = f.read()
print a
f.close()
```

## Good

```python
with open('file.txt') as f:
    for line in f:
        print(line)
```

[slide style="background-color:#2C3F51"]

# 什么是装饰器 {:&.flexbox.vleft}

> Python中的装饰器本质上就是在不改变函数本身的情况下
> 包装一个函数成为另一个函数的语法糖


```python
def wrapper(func):

    def inner(*args, **kwargs):
        print(func.__name__, *args, **kwargs)
        return func(*args, **kwargs)

    return inner

@wrapper
def print_func(words):
    return words


print_func('Hello decorator!')
```

[slide style="background-color:#2C3F51"]

# 装饰器有什么用？ {:&.flexbox.vleft}

> 在我看来本质上就是减少代码重复(Don't repeat yourself)，让代码的可读性更好!

```python
def get_article_detail(uid):
    article = ORM.get_article(uid)

    if article:
        cache.incr('key')

    return article
```

*使用装饰器*

```python
def increase_page_view(func):

    def wrapper(*args, **kwargs):
        obj = func(*args, **kwargs)
        if obj:
            cache.incr(obj.id)
        return obj

    return wrapper


@increase_page_view
def get_article_detail(uid):
    return ORM.get_article(uid)
```

> 这样原来的获取文章详情的函数，只关心获取文章，
> 而累加浏览量的操作放到具体的装饰器函数中，提高代码的可读性

[slide style="background-color:#2C3F51"]

# 使用pylint做代码质量检测 {:&.flexbox.vleft}

## pep8 https://www.python.org/dev/peps/pep-0008/

## Google python style guide http://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_language_rules/

[slide style="background-color:#2C3F51"]

## 谢谢

[Python 指南](http://pythonguidecn.readthedocs.io/zh/latest/writing/style.html)


----

Github：https://github.com/istommao/lecturenotes
