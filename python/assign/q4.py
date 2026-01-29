'''Write a Python program to check if a number is positive, negative or zero.'''
num = int(input("Enter your number: "))
if num>0:
    print(f"Your number {num} is:= positive")
elif num<0:
     print(f"Your number {num} is:= negative")
elif num==0:
      print(f"Your number {num} is:= zero")
else:
     print("please check your , its may be incorrect")