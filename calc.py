def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

# x=int(input("ENTER X : "))
# y=int(input("ENTER Y : "))
# n=int(input("ENTER 1 for sum , 2 for sub , 3 for mul , 4 for div : "))
x = 3
y = 4 
n = 1
if n == 1:
   a = add(x,y)
   print(a)
elif n == 2:    
   b = subtract(x,y)
   print(b)
elif n == 3:
  c =  multiply(x,y)
  print(c)
else :
  d = divide(x,y)        
  print(d)