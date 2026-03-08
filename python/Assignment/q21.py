'''Write a Python program to add 'in' at the end of a given string (length 
should be at least 3). If the given string already ends with 'ing' then 
add 'ly' instead if the string length of the given string is less than 3, 
leave it unchanged.'''

s1=input("Enter your string: ")
if len(s1) >=3:
    if s1[-3::]=="ing":
        new_s1=s1[:-3]+"ly"
        print(new_s1)
    else:
        s1+="in"
        print(s1)
else:
    print(s1)