#This is a comment, we use the #to indicate comments in python

""" This is a multiline comment """

#Python statements
Print("Welcome to my github repository") #This is a statement

#Many statement
print("Welcome !")
print("Lets dive into Python")
print("what should we begin with?") #These are  multiple statements


print("This is an example "); print("of multiple statement"); print("in python") #this is also an example of multiple statements


print("That is all about statements")
print("Thanks for your time")
print("Remember to stay with  us as we move to the next topic")


#Python output

"""Print text"""

"""we use the print() function to output text"""

print("This is a text")

print("Welcome back to the course")
print("Today we are learning about printing text")

print("Texts in python must be inside double quotes")
print('You can also insert them inside single quotes')

print("Python programming ", end = " ")
print("is awesome") #You can use the end parameter to print multiple words on the same line


"""print numbers """
"""we use the print function to print numbers in python but unlike text we dont put numbers in double quotes or single quotes"""

print(3)
print(1000)
print(5.0)

print(3 + 5)
print(4 * 8)

#you can mix text and numbers
print("The company was formed", 15,"years ago")

"""ython varaiables"""
#in python we create variables by assigning values to them

x = 24
y = "age"
print(x)
print(y)

"""Many values to multiple variables"""
x,y,z = "plates","knife","cups"
print(x)
print(y)
print(z)


k, m, n = "chairs" , "tables" , "cupboard"
print(k)
print(m)
print(n)


"""one value to multiple variables """
x = y = z ="plates"
print(x)
print(y)
print(z)


k = m = n = "chair"
print(k)
print(m)
print(n)

fruits = ["bananas","apples","mangoes"]
fruits = x,y,z
print(x)
print(y)
print(z)

"""Output variables"""
#We  use the print() function to output variables

x = "python is awesome"
print(x)

x = "Python "
y = "is"
z = "fun"

print(x,y,z) # we can output muliple variables by separating them by a comma 

x = "Python "
y = "is"
z = "fun"
print (x + y + z)

"""Global variables"""
x = "awesome"
def myfunc():
  print("python is " + x)
myfunc()

x = "awesome"
def myfunc():
  x = "fantastic"
  print("python is " +  x)
myfunc()
print("python is " + x)


def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)






