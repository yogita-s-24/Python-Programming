# Indentation - Indentation means whitespace at the beginning od a line to define scope in the code.

### 1. if statement
#Syntax : if condition :
#         __ statement-1
#         __ statement-2
#         __ statement-3
#         __ statement-4

#Example 1

a = 20
b = 20
if a==b:
  print("a and b are equal")
#OutPut: a and b are equal

#Example 2

a = 20
b = 10
if a==b:
  print("a and b are equal")
else:
   print("a and b are not equal")
#a and b are not equal

#Example 3

a = 20
b = 40
if a>b:
  print("a is greater")
else:
   print("b is greater")
#Output : b is greater

#Example 4

a = 10
b = 30
if a>b:
  print("a is greater")
else:
   print("b is greater")
#Output:   b is greater

#Example 5

a = 20
b = 10
if a>b:
  print("a is greater than b")
else:
   print("b is greater than a")
#Output: a is greater than b


# = - is used to assign value
# == - is used to check value is equal or not


#Assignment -8

#1. Write a program to check whether applicant is eligible for voting or not using if statement.

age = int(input("Enter Your Age :"))
if age >= 18:
  print("You are eligible for voting")
#Output : 
# Enter Your Age :19
# You are eligible for voting


#by using if-else statement
age = int(input("Enter Your Age "))
if age >= 18:
  print("Your age is {}. You are eligible for voting".format(age))
else:
  print("Your age is {}. You are not eligible for voting".format(age))
#Output: Enter Your Age 12
#        Your age is 12. You are not eligible for voting


#2. Write a program to check whether entered number is even ir odd by using if-else statements.
number = int(input("Enter Number = "))
if number % 2 == 0:
  print("{} is even.".format(number))
else:
  print("{} is odd.".format(number))
#Output : Enter Number = 12
#         12 is even.