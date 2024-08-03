thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# Print all key names in the dictionary, one by one:
for i in thisdict:
    print(i)
for x in thisdict.keys():
  print(x)
# Print all values in the dictionary, one by one:
print("\n")
for j in thisdict:
    print(thisdict[j])
for k in thisdict.values():
   print(k)
# Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x, y)