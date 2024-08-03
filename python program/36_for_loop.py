fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
print("looping through a string")
for x in "banana":
  print(x)
print("With the break statement we can stop the loop before it has looped through all the items:")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
print("With the continue statement we can stop the current iteration of the loop, and continue with the next:")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
print("range")
for x in range(1,10,2):
  print(x)
print("else with for loop")
for x in range(6):
  print(x)
else:
  print("Finally finished!")
print(" The else block will NOT be executed if the loop is stopped by a break statement.")
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
print("nested loop")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)