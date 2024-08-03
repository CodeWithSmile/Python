# list1=[30,30]
# list2=list1
# print(list2)
# print(id(list1))
# print(id(list2))
str='''
You cannot copy a list simply by typing list2 = list1, because: list2 will 
only be a reference to list1, and changes made in list1 will automatically 
also be made in list2.'''
print(str)
list1=[10,20,30,0]
listcopy=list1.copy()
print(listcopy)
s='''
Another way to make a copy 
is to use the built-in method list().'''
print(s)
thelist=[20,30,40]
newlist=list(thelist)
print(newlist)


