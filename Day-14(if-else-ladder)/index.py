# Day-14
#hsc>60 and jee>120
## 1. and operator
hsc = 80
jee = 140
result = hsc>60 and jee>120
print(result)
#Output: True


## 2.  OR
## 2. OR
hsc = 80
jee = 140
result = hsc>60 or jee>120
print(result)
#Output: True


## 3. if-else-ladder
num = int(input("Enter your name = "))
if num==1:
  print("You select option 1")
elif num==2:
   print("You select option 2")
elif num==3:
   print("You select option 3")
elif num==4:
   print("You select option 4")
elif num==5:
   print("You select option 5")
else:
   print("You select wrong option")
   
#Output: 
# Enter your name = 5
# You select option 5


#Example : 

alphabets = input("Enter your name = ")
if alphabets=='A':
  print("You select option A")
elif alphabets=='B':
   print("You select option B")
elif alphabets=='C':
   print("You select option C")
elif alphabets=='D':
   print("You select option D")
elif alphabets=='E':
   print("You select option E")
else:
   print("You select wrong option")

#Output : 
# Enter your name = D
# You select option D


for i in range(5):
  print("Hello World !!")
  
# Output :
# Hello World !!
# Hello World !!
# Hello World !!
# Hello World !!
# Hello World !!


while test_expression:
    Body of while
    
    while expression:
    statement(s)
    
num = int(input("Enter Any Number :"))
count = 0
while num>0:
  num = num // 10
  count = count + 1
print("Total Digits: ",count)

# Output: 
# Enter Any Number :63465346
# Total Digits: 8