'''Write a Python program to check whether a list contains a sub list'''

main_list = [1, 2, 3, 4, 5,[4,5]] 
for i in main_list:
    if type(i)==list:
        print("exist")
        break
else:
    print("not")