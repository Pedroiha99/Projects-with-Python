#Learn to Think Like a Programmer with Python.
#My first program.

print("hello world.")

#Variables, expressions and statements.
#Values and types.

#We can know what type of variable it is with the following function.   

msj = "hello world"
type(msj) #You must remember that we have to print the result.
print(type(msj))

#variable types.

a = 5
b = 11.5
msgs = "hi my friend"

print(type(a)) #integer type
print(type(b)) #type float
print(type(msgs)) #string type

#Python has 28 reserved words:
"""
and         continue       else        for         import          not         raise
assert      def            except      from        in              or          return
break       del            exec        global      is              pass        try
class       elif           finally     if          lambda          print       while
"""

#El orden de las operaciones
"""Las operaciones tiene un orden de ejecucion. Primero son las operaciones que estan estre parentesis, despues la exponenciacion,
#multiplicacion y division. Los operadores se evaluan de izquierda a derecha."""

#functions
""" a function is like the one used (type(msg)). There are built-in functions but there are also special functions which are
calls from their libraries. Below is an example, pay close attention to the syntax """

import math

b = math.cos(math.pi)

msg2 = "the cosine of pi is = "
print(msg2, b)

#Add new functions.
"""In programming contexts, function is a sequence of instructions with
name, which carries out the desired operation. This operation is specified in
a definition of function. example."""

def my_f(a, b):
    suma = a + b
    return suma

a = 5
b = 2

msg = "the sum of a + b is ="
c = my_f(a, b)
print(msg, c)

"""Variables and parameters are local
When you create a variable inside a function, it only exists inside that function.
function, and you cannot use it outside of it. For example, the function """

#Conditionals and recursion
"""The modulo operator works with integers (and integer expressions), and returns
the rest of dividing the first operand by the second."""

print("en este caso al dividir 10/2 el residuo es = ", 10 % 2, " y el resultado de dividir 10/3 = ", 10 % 3)

#Boolean expressions
"""A Boolean expression is an expression that is true or false. In Python,
an expression that is true has the value 1, and an expression that is false has
the value 0."""

print(5 == 5)
print(5 == 6)

"""
x != y          # x is not equal to y
x > y           # x is greater than y
x < y           # x is less than y
x >= y          # x is greater than or equal to y
x <= y          # x is less than or equal to y

A common mistake is to use a sign
single equal (=) instead of double (==). Remember that = is an operator
assignment and == is a comparison operator
"""

#Logical operators
"""There are three logical operators: and, or, and not."""

x = 5
y = 5
z = 6 

print("if x is equal to y or x is equal to z", x == y or x ==z)

#Conditional execution
"""To write useful programs, we almost always need the ability to check certain 
conditions and change the program's behavior accordingly. Conditional statements give us this ability. The most
simple is the if statement"""

a = 10

if a > 0:
    print(a, " is greater than zero")
    
if a % 2 == 0:
    print (a, "is even")
else:
    print (a, "is odd")
    
#Chained conditions
"""Sometimes there are more than two possibilities and we need more than two branches. A
way to express such a computation is a chained conditional:"""

x = 10
y = 20

if x < y:
    print (x, "is less than", y)
elif x > y:
    print (x, "is greater than", y)
else:
    print (x, "y", y, "are equal")

#Nested conditions
"""A condition can be nested within another. We could have written like this
example"""

x = 10
y = 20

if x == y:
     print (x, "y", y, "are equal")
else:
     if x < y:
         print (x, "is less than", y)
     else:
         print (x, "is greater than", y)

"""These are three ways to write the same operation"""

x = 8

if 0 < x:
    if x < 10:
        print ("x is a one-digit positive number.")

if 0 < x and x < 10:
    print ("x is a one-digit positive number.")
    
if 0 < x < 10:
    print ("x is a one-digit positive number.")
    
#The return statement
"""The return statement allows you to terminate the execution of a function before
reach its end. One reason to use it is to detect an error condition:"""

import math

x = 7 

def printLogarithm(x):
    if x <= 0:
        print ("Positive numbers only, please.")
        return
    
result = math.log(x)
print ("The log of ",x ," is ", result)

#Recursion
"""It may not be obvious why this is good, but
It turns out to be one of the most interesting and curious things you can do.
A program. Examine for example the following function:"""

n = 10

def countdown(n):
    if n == 0:
        print ("Taking off!")
    else:
        print (n)
        countdown(n-1)
    
countdown(n)

#keyboard input
"""Python provides internal functions that obtain input from the keyboard. example."""

name = input("what's your name?")
print("hello", name)

num = int(input("enter your favorite number: "))
print("your favorite number is: ", num)

#Return values
"""In a productive function it is a good idea to make sure that any possible
program path reaches a return statement. For example:"""

x = int(input("enter a number: "))

def absolutevalue(x):
    if x < 0:
        return -x
    elif x > 0:
        return x
    else:
        return -1 
    
print("the absolute value of ", x, " is ", absolutevalue(x))   

#More recursion factorial

n = int(input("Enter a number to know its factorial: ")) 

def factorial(n):
    if n == 0:
        return 1
    else:
        recursive = factorial (n-1)
        result = n * recursive
        return result
    
#One more example fibonacci

n = int(input("Enter a number and know its Fibonacci series: "))

def fibonacci (n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)   
    
#Iteration
#The while statement

def countdown(n):
    while n > 0:
        print (n)
        n = n-1
        
print ("Taking off!")


#Boards 
"""The tab character causes the cursor to move to the right until
reach one of the tab stop markers. remember to import the math library in this example"""

x = 1.0

while x < 10.0:
    print (x, "\t", math.log(x))
    x = x + 1.0










