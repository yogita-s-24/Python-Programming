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