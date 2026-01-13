Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
print("hello ,welcome to python programming!")
hello ,welcome to python programming!
a = int(input("enter first number :"))
enter first number :20
b = int(input("enter two number :"))
enter two number :10
sum = a + b
print("sum=",sum)
sum= 30
num = int(input("enter a number :"))
enter a number :25
if num % 2 == 0:
    print("The Number is Even")
else:
    print("Not a Leap year")

    
Not a Leap year
print("Value of PI =",math.pi)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print("Value of PI =",math.pi)
NameError: name 'math' is not defined. Did you forget to import 'math'?
print("Value of PI = ",math.pi)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print("Value of PI = ",math.pi)
NameError: name 'math' is not defined. Did you forget to import 'math'?
import math
print("value of p1 = " ,math.pi)
value of p1 =  3.141592653589793
PI = 3.14
print("Constant value of PI =",p1)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print("Constant value of PI =",p1)
NameError: name 'p1' is not defined
>>> print("constant value of PI =",PI)
constant value of PI = 3.14
>>> num = int(input("Enter a number :"))
Enter a number :30
>>> square = num * num
>>> print("square =",square)
square = 900
>>> radius = float(input("enter radius :"))
enter radius :20
>>> area = 3.14 * radius * radius
>>> print("Area of circle =".area)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print("Area of circle =".area)
AttributeError: 'str' object has no attribute 'area'
>>> print("Area of circle =",area)
Area of circle = 1256.0



