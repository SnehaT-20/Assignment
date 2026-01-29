'''Write a Python program to get unique values from a list'''

numbers = [11,20,24,10,90,80,11,20]
unique_list = []
for i in numbers:
    if i not in unique_list:
        unique_list.append(i)
print("Unique values:", unique_list)