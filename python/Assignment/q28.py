'''Differentiate between append () and extend () methods?

=>  append() Method:==
        - Adds a single element to the end of the list.
        - Modifies the original list
        - The element can be any data type (number, string, list, etc.)
        - If you append from another list then that whole list will append means nested list.
         
=>  extend() Method:==
        - Adds elements of another iterable (list, tuple, string, etc.) to the end of the list individually.
        - Modifies the original list
        - If you extend single element(in string) to list then each and every character of that element is added separately.
        - If you extend from another list then each element of the iterable is added separately.
'''

print("---------APPEND EXAMPLE-------------")
list1=[1,2,3]
list1.append(4)
print(list1)  # Output: [1, 2, 3, 4]

list1.append([5, 6])
print(list1)  # Output: [1, 2, 3, 4, [5, 6]]

print("---------EXTEND EXAMPLE-------------")
 
list1.extend([4, 5])
print(list1)  # Output: [1, 2, 3, 4, 5]

list1.extend("hi")
print(list1)  # Output: [1, 2, 3, 4, 5, 'h', 'i']