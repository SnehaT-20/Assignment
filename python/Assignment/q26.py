'''How will you remove last object from a list?

=> we can remove last element or object in multiple way:
    - Using pop() method
        my_list.pop() 
    
    - Using del statement
        del my_list[-1]
    
    - Using slicing (creates a new list)
        my_list = my_list[:-1]
'''
lst_city=["dwarka","rajkot","ahemdabad","ab"]
lst_city.pop()
print(lst_city)