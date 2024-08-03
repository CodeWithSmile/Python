a={1,'one',2,'two'}
b={11,'el',12,'tw'}
print(a)
a.add(3)
print(a)
a.update(b)
print(a)
# If the item to remove does not exist, remove() will raise an error.
a.remove(3)
print(a)
# If the item to remove does not exist, discard() will NOT raise an error.
a.discard("tw")
print(a)
# You can also use the pop() method to remove an item, 
# but this method will remove a random item, so you cannot be sure what item that gets removed.
x=a.pop()
print(x)
print(a)
# The clear() method empties the set:
c={1,3,4,5}
print(c)
c.clear()
print(c)
# The del keyword will delete the set completely:
d={2,4,5}
print(d)
del d
# print(d) raise an error
