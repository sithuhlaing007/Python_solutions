num=int(input("Enter a number : "))
def fibonacci_of(n):
     if n in {0, 1}:  # Base case
         return n
     return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
for n in range(num):
  print(fibonacci_of(n))
# for example 
# input 
# num = 6
# output
# 0
# 1 
# 1
# 2 
# 3 
# 5