# The self Parameter
#
# The self parameter is a reference to the current instance of the 
# class, and is used to access variables that belongs to the class.

# It does not have to be named self , you can call it whatever you like,
# but it has to be the first parameter of any function in the class:
class Person:
  def __init__(mysillyobject, name, age):#first paramerter act like self mysilliobject & abc
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)
    print("Hello my age is " ,abc.age)
p1 = Person("John", 36)
p2=Person("jiya",90)
# p1.age=22     
# modify the object property
# del p1.age
# delete the object property
del p2
p1.myfunc()
p2.myfunc()