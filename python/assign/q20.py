'''Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string'''

s1 = input("Enter your first string: ")
s2 = input("Enter your second String: ")

new_s1 = s2[:2] + s1[2:]
new_s2 = s1[:2] + s2[2:]

result = new_s1 + " " + new_s2
print(result)