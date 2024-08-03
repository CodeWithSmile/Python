# f = open("demofile.txt","x")

#first create the file
# f = open("demofile.txt","r")

# print(f.read())#to read full file
# print(f.readline())#to read single line
# print(f.readlines())#to read all lines
# print(f.read(5))#to read 5 word

##to write into the file it delete previous content
# f=open("demofile.txt","w")
# f.write("good morning")
# f.close()

# #append at the end of the file
# f=open("demofile.txt","a")
# f.write("\ngood morning india")
# f.close()

# f=open("demofile.txt","r")
# print(f.read())


#to remove the file
# f = open("myfile.txt", "x")
# import os
# os.remove("myfile.txt")

import os
if os.path.exists("myfile.txt"):
  os.remove("myfile.txt")
else:
  print("The file does not exist")
