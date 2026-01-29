'''Write a Python program that will return true if the two given 
integer values are equal or their sum or difference is 5'''
num1=int(input("Enter your first number:= "))
num2=int(input("Enter your second number:= "))
if num1==num2:
    print("true")
elif num1+num2==5 or num1-num2==5:
    print("true")
else:
    print("false")