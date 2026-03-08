'''What is List? How will you reverse a list?

=>  A list is a ordered collection of items in a single variable.
=>  List are mutable means you can change, add, remove the elements of lists.
=>  List can contain different data type elements.
=>  Eg: my_list = [10, "Python", 3.14, True]
=> You can reversed the list in multiple ways:
    - Using reverse() method (in-place)
        list.reverse()

    - Using slicing
        list[::-1]

    - Using reversed() function
        reversed(list)

    - Using sort function
        list.sort(reverse=True)
'''

lst_city=["dwarka","rajkot","ahemdabad","ab"]
lst_city.sort(reverse=True)
print(lst_city)