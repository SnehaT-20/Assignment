'''Write a Python program to unzip a list of tuples into individual lists.'''

data = [(1, 2), (3, 4), (5, 6)]
list1, list2 = zip(*data)
list1 = list(list1)
list2 = list(list2)
print(list1)
print(list2)