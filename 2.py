Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=dict()
type(x)
<class 'dict'>
x={}
keys=['a','b','c','d']
values=[1,2,3,4]
dictionary=dict(zip(keys,values))
d=dict(name='张三',age=20)
aDict=dict.fromkeys(['name','age','sex'])
aDict
{'name': None, 'age': None, 'sex': None}
aDict={'age':20,'score':[98,97],'name':'张三','sex':'男'}
aDict['age']
20
aDict['address']
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    aDict['address']
KeyError: 'address'
