#Day-12
#Comparision operator / Relational operator
# 1. equal to (==)
# 2. less than (<)
# 3. greater than(>)
# 4. less than or equal to (<=)
# 5. greater than or equal to (>=)

# 1. equal to (==)
#Example 1
a = 10
b = 10
result = a==b
print(result)
#Output : True

#Example 2
a = 10
b = 1
result = a==b
print(result)
#output: False


# 2. less than (<)

#Example 1

a = 10
b = 11
result = a<b
print(result)
#Output: True

#Example 2

a = 15
b = 11
result = a<b
print(result)
#Output: False


# 3. greater than(>)
#Example 1

a = 10
b = 13
result = a>b
print(result)
#Output: False

#Example 2

a = 15
b = 13
result = a>b
print(result)
#Output: True


# 4. less than or equal to (<=)
#Example 1
a = 20
b = 20
result = a<=b
print(result)
#Output: True

#Example 2
a = 10
b = 20
result = a<=b
print(result)
#Output: True

#Example 3
a = 30
b = 20
result = a<=b
print(result)
#Output: False


# 5. greater than or equal to (>=)
#Example 1
a = 30
b = 30
result = a>=b
print(result)
#Output: True

#Example 2
a = 50
b = 60
result = a>=b
print(result)
#Output:False


# not equal to (!=)
#Example 1
a = 30
b = 30
result = a!=b
print(result)
#Output: False

#Example 2
a = 20
b = 30
result = a!=b
print(result)
#Output: True


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