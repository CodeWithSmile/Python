a=[10,20,30,40,50]
print(a)#list1 integer
b=["apple","banana","mango"]
print(b)#list2 string
c=["pink",1,"yellow",2,"red",3]#list3 combo
print(c)
d=list((1,2,3,'hi'))#list 4 list-constructor
print(d)
print("list a[1]=",a[1])#positive index
print("list a[-1]=",a[-1])#negative index
print("list a[1:3]=",a[1:3])#range
print("list a[1:]=",a[1:])
print("list a[:3]=",a[:3])
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:#check item present in list or not
  print("Yes, 'apple' is in the fruits list")
print("change item value")
thislist[1] = "blackcurrant"
print(thislist)
print("change the range of item values")
thislist[1:3]=["cherry","strawberry"]
print(thislist)
print("delete existing item 1 & 2 both occupy one item")
thislist1 = ["apple", "banana", "cherry"]
thislist1[1:3] = ["watermelon"]
# print(thislist1[2])
print(thislist1)
print("insert function")
thislist.insert(2,"mango")#it display 4 item it cant delete existing item 
print(thislist)#existing item shift to next index position
print("append")#append to last index position
thislist.append("pineapple")
print(thislist)
thislist.append(thislist1)
print(thislist)
print("remove list item")
a.remove(10)
print(a)
print("pop item by using index number")
print(a.pop(1))
print(a)
print("pop last item")
print(a.pop())
print(a)
print("deleting item")
del a[1]
print(a)
# del a
# print(a)#raise error list no present
print("clear the list")
b.clear()
print(b)