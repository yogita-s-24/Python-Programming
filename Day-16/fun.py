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

#Output :
# Enter Principle : 80
# Enter Rate : 500
# Enter time : 90
# 36000.0

#2. Arguments but No Return

def cal_si(p,r,t):
  si = p*r*t/100
  print(si)

Amount = int(input("Enter Amount : "))
Rate = int(input("Enter Rate : "))
Time = int(input("Enter Time : "))
cal_si(Amount, Rate, Time)

# Output :
# Enter Amount : 2000
# Enter Rate : 70
# Enter Time : 120
# 168000.0

#3. No Arguments but Return:

def cal_si():
  p = int(input("Enter Principle : "))
  r = int(input("Enter Rate : "))
  t = int(input("Enter time : "))
  si = p*r*t/100
  return si

ans = cal_si()
print(ans)

# Output :
# Enter Principle : 12
# Enter Rate : 1000
# Enter time : 120
# 14400.0

#4. Arguments And Return

def cal_si(p, r, t):
  si = p*r*t/100
  return si

Amount = int(input("Enter Amount : "))
Rate = int(input("Enter Rate : "))
Time = int(input("Enter Time : "))
ans = cal_si(Amount,Rate, Time)
print(ans)

# Output of Program:
# Enter Amount : 100
# Enter Rate : 200
# Enter Time : 90
# 18000.0

