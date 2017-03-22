title: python idiom
speaker: silence
url: https://github.com/ksky521/nodePPT
transition: vertical3d
files: /js/demo.js,/css/demo.css

[slide style="background-color:#2C3F51"]

# python idiom
## Author：silence


[slide style="background-color:#2C3F51"]

# 概览 {:&.flexbox.vleft}

- 检查变量是否等于常量
- 编写函数的几个原则
- 列表推导式
- 善用装饰器
- 分清 == 与 is 的适用场景
- 数据交换值的时候不推荐使用中间变量
- 连接字符串应优先使用 join 而不是 +
- 元素是否存在字典中
- 使用 enumerate() 获得列表中的当前位置的计数
- 使用 with 读取文件


[slide style="background-color:#2C3F51"]

# 元素是否存在字典中 {:&.flexbox.vleft}

## Bad

```python
datadict = {'name': 'tommao', 'age': 25}
'name' in datadict.keys()

datadict.has_key('name')
```

## Good

```python
datadict = {'name': 'tommao', 'age': 25}
'name' in datadict
```


[slide style="background-color:#2C3F51"]

# 连接字符串应优先使用 join 而不是 + {:&.flexbox.vleft}

```python
strlist = ['a', 'b', 'c']
strs = ''.join(strlist)
```


[slide style="background-color:#2C3F51"]

# 检查变量是否等于常量 {:&.flexbox.vleft}


## Bad


```python
if attr == True:
    print 'True!'

if attr == None:
    print 'attr is None!'
```

## Good

```python
if attr:
    print 'attr is truthy!'

# 或者做相反的检查
if not attr:
    print 'attr is falsey!'

# or, since None is considered false, explicitly check for it
if attr is None:
    print 'attr is None!'
```


[slide style="background-color:#2C3F51"]

# 数据交换值的时候不推荐使用中间变量 {:&.flexbox.vleft}

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
        print line
```

[slide style="background-color:#2C3F51"]

## 谢谢

----

Github：https://github.com/istommao/lecturenotes
