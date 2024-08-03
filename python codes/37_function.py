def my_function():
  print("Hello from a function")
my_function()

print("-parameter-")
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

print("-arbitary argumets-")
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

print("-keyword arguments-")
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

print("-arbitary keyword argument-")
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

print("-default arguments-")
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

print("passing list as an argument")
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

print("-return-")
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

print("positional only argument")
# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments:
def my_function(x, /):
  print(x)

print("Keyword-Only Arguments")
def my_function(*, x):
  print(x)
my_function(x = 3)

print("combine keyword-only and positional")
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)
my_function(5, 6, c = 7, d = 8)

