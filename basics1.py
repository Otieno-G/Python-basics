#Data types
"""We use the type() function to get the data type of an object """

import random
print(random.randrange(2,10))  #We use it to make random numbers



x = 12
y = 6.82
z = "Lets code together"

print(type(x))
print(type(y))
print(type(z))

#Numbers

x = 45
print(x) #integer
print(type(x))

b = -26
print(b) #integer
print(type(b))

y = 4.28
print(y) #float
print(type(y))
      
v = 18e2
print(v) #float
print(type(v))

a = 42E3
print(a)  #float
print(type(a))
      

z =  8j #complex
print(z)
print(type(z))
      
f = 18j
print(f) #complex
print(type(f))
      
t = 5+9j
print(t) #complex
print(type(t))

#Type conversion
"""we can use the int(),float(),complex to conver from one data type to another
//we can not conver complex numbers to another number type"""
a = 23
b = 3.14
c = 16j

a = int(b)
b = float(a)
c = complex(b)

print(a)
print(b)
print(c)


x = 5
y = 22.20
z = 2+3j

print(type(x))
print(type(y))   
print(type(z))


age = 26
print(int(age))
print(float(age))
print(str(age))



      
      
