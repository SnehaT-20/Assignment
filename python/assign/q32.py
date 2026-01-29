'''Write a Python program to remove duplicates from a list.'''

lst=["aba","xy","1221","ss","aaaaaa","123","america","aba","aaaaaa"]
new_list = []
for i in lst:
    if i not in new_list:
        new_list.append(i)
print(new_list)
