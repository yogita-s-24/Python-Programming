#Day-13

rate, quantity = input("Enter rate and quantity").split()
bill = int(rate) * int(quantity)
if bill > 500:
  print("#### 20% ####")
  print("Actual Bill",bill)
  discount = (bill/100)*20
  print("Discount :",discount)
  print("Payable Ammount :",bill - discount)
else :
  print("#### 5% ####")
  print("Actual Bill",bill)
  discount = (bill/100)*5
  print("Discount :",discount)
  print("Payable Ammount :",bill - discount)
  
# Output:
# Enter rate and quantity12 4
# #### 5% ####
# Actual Bill 48
# Discount : 2.4
# Payable Ammount : 45.6

# Example in short

rate, quantity = input("Enter rate and quantity").split()
bill = int(rate) * int(quantity)
disc_per = 0

if bill>500:
  disc_per = 20
else :
  disc_per = 5

discount = (bill/100)*disc_per
paybleAmount = bill - discount
print("##### {} OFF #####".format(disc_per))
print("Actual Bill",bill)
print("Discount",discount)
print("Payable Amount",paybleAmount)

#Output:
# Enter rate and quantity12 20
# ##### 5 OFF #####
# Actual Bill 240
# Discount 12.0
# Payable Amount 228.0