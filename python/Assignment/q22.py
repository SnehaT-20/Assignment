'''Write a Python function to reverses a string if its length is a multiple 
of 4.'''

s1=input("Enter your string: ")
if len(s1)%4==0:
    print(s1[::-1])
else:
    print("Length of string is not a multiple of 4")