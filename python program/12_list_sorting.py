print("sorting alphabetically")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
print("sort list numericaly")
a=[20,40,30,10,50]
a.sort()
print(a)
print("sorting desending alphabets")
thislist.sort(reverse=True)
print(thislist)
print("sorting decending numeric")
a.sort(reverse=True)
print(a)
print("customizing sort function")
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
print("By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:")
print("sort is case sensitive")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
print("key attribute can avoid this capital sorting problrm")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
print("reverse")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)