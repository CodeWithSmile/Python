try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

  #else block
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

  #finally
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# Try to open and write to a file that is not writable:
try:
  f = open("demofile1.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
 
 #raise 
  x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

#raise type error
y = "hello"

if not type(y) is int:
  raise TypeError("Only integers are allowed")