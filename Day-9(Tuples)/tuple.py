# Tuples is used to store multiple values in single variables.
# tuple are store in parenthesis ()

# Properties of tuples:
# 1. Ordered
# 2. Unchangable 
# 3. Allow duplicates

# Example 1 :

myBasket = ("Apple", "Banana", "Graphs", "Orange")
print(myBasket)

# output : ('Apple', 'Banana', 'Graphs', 'Orange')

# * Manipulation of tuple : 

# we created variable myBasket and store the values and created another variable for converting tuples into list 

# tuples==>list==>update==>tuple

# Example 2 :

myBasket = ("Apple", "Banana", "Graphs", "Orange")
listMyBasket = list(myBasket)
listMyBasket[0] = "Cherry"
myBasket = tuple(listMyBasket)
print(myBasket)

# output : ('Cherry', 'Banana', 'Graphs', 'Orange', 'Apple)

# Example 3 :

pystudent = ("Saurabh", "Harshu", "Yogii")
print(pystudent.index("Saurabh"))

#Output : 0

# Example 4 :

pystudent = ("Saurabh", "Harshu", "Yogii")
print(pystudent.index("Yogii"))

#Output : 2


# * Count Method

# Example 5:

pystudent = ("Saurabh", "Harshu","Harshu", "Yogii", "Yogii")
print(pystudent.count("Yogii"))

#Output : 2

# Example 6:

pystudent = ("Saurabh", "Harshu","Harshu", "Yogii", "Yogii")
print(pystudent.index("Saurabh"))

#Output : 1


# * Concatenation of String

