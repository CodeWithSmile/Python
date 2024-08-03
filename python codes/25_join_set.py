set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
print("union")
set3 = set1.union(set2)
print(set3)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
print("update")
set1.update(set2)
print(set1)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
# ///////////Keep ONLY the Duplicates
print("intersection")
z = x.intersection(y)
# x.intersection(y)
# print(x)
print(z)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print("intersection_update->common")
x.intersection_update(y)
print(x)
# /////////Keep All, But NOT the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print("symmetric_difference_update")
x.symmetric_difference_update(y)
print(x)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print("symmetric_diffrence")
z = x.symmetric_difference(y)
print(z)