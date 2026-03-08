'''How will you compare two lists?
=>  There are multiple ways:
    - Direct Comparison Using ==(check order as well)
    - Compare Lists Using a Loop(check odered as well)
    - Compare Lists Ignoring Order(ignore order)
    - Using set() for Unique Elements(ignore order nd duplicates)
'''
print("====Direct Comparison Using(==)========")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [3, 2, 1]
print(list1 == list2)  # True
print(list1 == list3)  # False

print("====Compare Lists Using a Loop========")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
equal = True
if len(list1) != len(list2):
    equal = False
else:
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            equal = False
            break
print(equal)  # True

print("====Compare Lists Ignoring Order========")
list1 = [1, 2, 3]
list2 = [3, 2, 1]
print(sorted(list1) == sorted(list2))  # True

print("====Using set() for Unique Elements========")
list1 = [1, 2, 3, 3]
list2 = [3, 1, 2]
print(set(list1) == set(list2))  # True