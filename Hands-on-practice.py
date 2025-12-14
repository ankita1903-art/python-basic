Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> print('Hello World')
Hello World
>>> a="My name is Ankita Roy"
>>> b="I am 22 years old."
>>> c="I live in Barrackpore."
>>> print(a,b,c)
My name is Ankita Roy I am 22 years old. I live in Barrackpore.
>>> print('Basic Calculation in python')
Basic Calculation in python
>>> a=10
>>> b=20
>>> sum=a+b
>>> print(sum)
30
>>> sub=b-a
>>> print(sub)
10
>>> mul=a*b
>>> print(mul)
200
>>> div=b/a
>>> print(div)
2.0
>>> d=b//a
>>> print(d)
2
>>> mod=b%a
>>> print(mod)
0
>>> #List of fav.foods
>>> foods=["EGG","NOODLES","PIZZA"]
>>> print("My favorite foods are",foods)
My favorite foods are ['EGG', 'NOODLES', 'PIZZA']
>>> foods=("EGG","NOODLES","PIZZA")
... print("My favorite foods are",foods)
SyntaxError: multiple statements found while compiling a single statement
>>> foods=list("EGG","NOODLES","PIZZA")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    foods=list("EGG","NOODLES","PIZZA")
TypeError: list expected at most 1 argument, got 3
>>> fruits = list(("apple", "banana", "cherry"))
>>> print(fruits)
['apple', 'banana', 'cherry']
