# list are store value in [] brakets

#List
students = ['Aachal','Aarav','Avinash','Dolly','Deva']
print(students)
#Output :['Aachal', 'Aarav', 'Avinash', 'Dolly', 'Deva']


#Slicing on List
#Example 1
students = ['Aachal','Aarav','Avinash','Dolly','Deva']
print(students[0:4])
#Output :['Aarav', 'Avinash', 'Dolly']


#Example 2
students = ['Aachal','Aarav','Avinash','Dolly','Deva']
print(students[4:])
#Output :['Deva']


#Example 3
students = ['Aachal','Aarav','Avinash','Dolly','Deva']
print(students[-2])
#Output : Dolly  (It is delete from last)

#Properties Of List
#1. Ordered - Lists are in ordered form, which means that the items have a defined order and that order will not change.

#Example 1
students = ['Aachal','Aarav','Avinash','Dolly','Deva']
print(students)
#Output :['Aachal', 'Aarav', 'Avinash', 'Dolly', 'Deva']


#2. Allow duplicates-Lists can have items with the same value. Lists can contain duplicate values.

#Example 1
fruits =['apple','banana','cherry','apple','banana']
print(fruits)
#Output:['apple', 'banana', 'cherry', 'apple', 'banana']


#3. List can contain different datatype - You can add differnent datatypes in single list.

#Example 1
randomData = ["abc",10,True,50.50,"Hii"]
print(randomData)
#Output: ['abc', 10, True, 50.5, 'Hii']


#4. Changeable - The list is changeable and we can change add and remove items in a list after it has been created.

# i. Update - Update (change) a list element at the specified index.

#Example 
courses = ["c","c++","python","javascript","icp"]
print("Befor update: ",courses)
courses[1] = "c++ programming"
print("After update :",courses)
#output: 
# Befor update: ['c', 'c++', 'python', 'javascript', 'icp']
#  After update : ['c', 'c++ programming', 'python', 'javascript', 'icp']


# ii.Insert - The insert() method insert an element at the specified position in the list.

#Example 
courses = ["c","c++","python","java","icp"]
print("before insert:", courses)
courses.insert(4,"Android Dev")
print("After insert :",courses)
# Output :
# Before insert: ['c', 'c++', 'python', 'java', 'icp']
# After insert : ['c', 'c++', 'python', 'java', 'Android Dev', 'icp']


# iii.Append - The append() method adds an element to the end of the list.

# Example :
courses = ["c","c++","python","java","icp"]
print("Before append :",courses)
courses.append("Android Dev")
print("After append :",courses)
# Output :
# Before append : ['c', 'c++', 'python', 'java', 'icp']
# After append : ['c', 'c++', 'python', 'java', 'icp', 'Android Dev']


# Remove - The remove() method removes the specified item in the lists.

# Example :
fruits = ['apple','banana','orange','cherry']
print("Before remove",fruits)
fruits.remove('banana')
print("After remove",fruits)
# Output :
# Before remove ['apple', 'banana', 'orange', 'cherry']
# After remove ['apple', 'orange', 'cherry']


# Pop - The pop() method remove the element. It takes a single argument (index).

# Example :
fruits = ['appple','banana','orange','cherry']
print("Before pop",fruits)
fruits.pop(2)
print("After pop",fruits)
# Output :
# Before pop ['appple', 'banana', 'orange', 'cherry']
# After pop ['appple', 'banana', 'cherry']


# Delete - The delete() method delete elements from the specified index.

# Example :
fruits = ["apple","banana","cherry","mango"]
print("Before delete : ",fruits)
del fruits[1]
print("After delete :",fruits)
# Output :
# Before delete : ['apple', 'banana', 'cherry', 'mango']
# After delete : ['apple', 'cherry', 'mango']