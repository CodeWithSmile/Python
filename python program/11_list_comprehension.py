fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print("without list comprehension")
print(newlist)
print("with list comprehension")
thelist=[print(x) for x in fruits if "a" in x]
print(thelist)
newlist=[x for x in range(10)]
print(newlist)