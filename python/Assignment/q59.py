'''Write a Python program to create a dictionary from a string. 
Note: Track the count of the letters from the string.'''
string=input("Enter your string: ")
dict1={}
for ch in string:
    if ch in dict1:
        dict1[ch] += 1
    else:
        dict1[ch] = 1
print(dict1)