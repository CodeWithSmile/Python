# You can change the value of a specific item by referring to its key name:
a={
    1:'one',
    2:'t',
    3:'three',
    4:'four' 
}
print(a)
a[2]="two"
print(a)
# The update() method will update the dictionary with the items from the given argument.
b={
    1:'one',
    2:'two',
    3:'three',
    4:'f' 
}
print(b)
b.update({4:'four'})
print(b)