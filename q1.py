#Question 1: Write a Python program to check if a string is a palindrome.
def pali(str):
  if str==str[::-1]:
    print(str,"is a plaiandrome")
  else:
    print(str,"is not a paliamdrome")

str="malayalam"
pali(str)