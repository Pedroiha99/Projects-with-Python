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





