#Day-16 Function
# There are four types of function
#1.No Arguments And No Return
#2. Arguments but No Return
#3. No Arguments but Return
#4. Arguments And Return


# HW-9

#1.No Arguments And No Return

def cal_si():
  p = int(input("Enter Principle : "))
  r = int(input("Enter Rate : "))
  t = int(input("Enter time : "))
  si = p*r*t/100
  print(si)
cal_si()

