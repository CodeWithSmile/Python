s="hii"
m="hello this is single line string"
n="""and this is multiline string
which is defined by using triple quotes"""
print(s)
print(m)
print(n)
#accesing string letter by using indexing
print(s[0])
print(s[1])
print(s[2])
#accesing string letter by using for loop
print("------using loop----------")
for i in s:
    print(i)
print("---------------multiline string------------")
#for j in m:
   #for k in j:
        #print(k)
#for j in m:
    #print(j)
#string starting & ending index
print(m[0:5])
#whole string
print(s[:])
#till end of the string
print(s[0:])
# length of the string
print(len(s))
#starting from default 0
print(s[:3])
#reversing string
print(s[::-1])
#negative index
print(s[-4:-2])
#

