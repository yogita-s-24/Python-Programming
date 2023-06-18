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