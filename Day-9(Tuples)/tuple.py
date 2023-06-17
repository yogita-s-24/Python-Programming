# Tuples is used to store multiple values in single variables.
# tuple are store in parenthesis ()

# Properties of tuples:
# 1. Ordered
# 2. Unchangable 
# 3. Allow duplicates

myBasket = ("Apple", "Banana", "Graphs", "Orange")
print(myBasket)

# output : ('Apple', 'Banana', 'Graphs', 'Orange')

# Manipulation of tuple : 

# we created variable myBasket and store the values and created another variable for converting tuples into list 

# tuples==>list==>update==>tuple

myBasket = ("Apple", "Banana", "Graphs", "Orange")
listMyBasket = list(myBasket)
listMyBasket[0] = "Cherry"
myBasket = tuple(listMyBasket)
print(myBasket)

# output : ('Cherry', 'Banana', 'Graphs', 'Orange', 'Apple)
