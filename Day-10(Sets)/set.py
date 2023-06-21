#Properties of sets -
# 1. Unordered - It has no specific order
mycolor = {'sky','pink','yellow','green'}
print(mycolor)

#Output : {'yellow', 'pink', 'sky', 'green'}


# 2.Unindexed - it no proper index always it change not allow duplicates
mycolor = {'sky','pink','yellow','green','green'}
print(mycolor)

#Output : {'yellow', 'pink', 'sky', 'green'}


# 3.unique value -

mycolor = {'orange','sky','pink','sky','green','sky','sky'}
print(mycolor)

#Output : {'pink', 'orange', 'sky', 'green'}


#SET
#add() method
mycolor = {'orange','sky','pink','sky','green'}
print("Before adding Value : ",mycolor)
mycolor.add('white')
print("After adding Value : ",mycolor)

#Output : Before adding Value :  {'pink', 'orange', 'sky', 'green'} 
#         After adding Value :  {'orange', 'sky', 'green', 'white', 'pink'}


#remove() method
#remove element to sets
#Hard removal- and Soft removal-

mycolor = {'orange','sky','pink','sky','green'}
print("Brfore remove : ",mycolor)
mycolor.remove('pink')
print("After remove :",mycolor)

#Output : Brfore remove :  {'pink', 'orange', 'sky', 'green'}
#         After remove : {'orange', 'sky', 'green'}


#hard removal method - in this method we used remove() it shows error bcz when value is not present
mycolor = {'orange','sky','pink','sky','green'}
print("Before remove : ",mycolor)
mycolor.remove('blue')
print("After remove :",mycolor)

#Output : error


#soft method - in this case we used discard method
mycolor = {'orange','sky','pink','sky','green'}
print("Brfore discard :",mycolor)
mycolor.discard('blue')
print("After discard :",mycolor)

#Output: Brfore discard : {'green', 'sky', 'pink', 'orange'}
#        After discard : {'green', 'sky', 'pink', 'orange'}


#Set methods
#union() method - not allow duplicates
colorList1 = {'sky','blue','white','black'}
colorList2 = {'yellow','green','red','sky'}
allElements = colorList1.union(colorList2)
print(allElements)

#Output: {'black', 'sky', 'red', 'blue', 'yellow', 'green', 'white'}


#intersection() methods - it find same elements
colorList1 = {'sky','blue','white','black'}
colorList2 = {'yellow','green','red','sky','black'}
sameElements = colorList1.intersection(colorList2)
print(sameElements)

#Output: {'sky', 'black'}


colorList1 = {'sky','blue','white','black'}
colorList2 = {'yellow','green','red','sky','black'}
sameElements = colorList1.symmetric_difference(colorList2)
print(sameElements)

#Output: {'blue', 'yellow', 'green', 'white', 'red'}
