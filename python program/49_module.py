import mymodule as md
md.greeting("good morning")
a=md.person1["age"]
print(a)
b=md.person1["name"]
print(b)
#built-in module
import platform
print(platform.system())

#from import 
from mymodule import person1

print(person1["age"])