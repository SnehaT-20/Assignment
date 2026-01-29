'''Write a Python program to get a string made of the first 2 and the last 
2 chars from a given a string. If the string length is less than 2, return 
instead of the empty string.'''

s1=input("Enter your string: ")
if len(s1)>=2:
    a=s1[:2:]+s1[-2::]     
    print(a)
else:
    print("")