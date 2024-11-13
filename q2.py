#Question 2: Write a Python program to find the factorial of a number.
num=4
fact=1
for i in range(num,0,-1):
  fact*=i
print(fact)