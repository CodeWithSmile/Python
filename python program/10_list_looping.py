a=['banana','mango','apple']
print("--simple for loop--")
for i in a:
    print(i)
print("--range and len function--")
for i in range(len(a)):
    print(a[i])
print("---while loop=---")
i=0
while i<len(a):
    print(a[i])
    i=i+1
print("---list comprehension----")
[print(i) for i in a]
