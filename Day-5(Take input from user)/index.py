# Taking input from user
# Example 1

val1 = input("Enter value 1 :")
val2 = input("Enter value 2 :")

sum = val1 + val2
print(sum)

# sum = in string format
# This program print output in string, it is not added two values

# Example 2

val1 = int(input("Enter value 1 :"))
val2 = int(input("Enter value 2 :"))

sum = val1 + val2
print(sum)


# O/p = val1 + val2 = sum

# OR

# Example 3

val1 = input("Enter value 1 :")
val2 = input("Enter value 2 :")

sum = int(val1) + int(val2)
print(sum)


# Example 4

# Out put in formated way 

val1 = input("Enter value 1 :")
val2 = input("Enter value 2 :")

sum = int(val1) + int(val2)
print("Sum of { } and { } is { }".format(val1,val2,sum))

