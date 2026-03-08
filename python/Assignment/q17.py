'''What are negative indexes and why are they used?

=>  In Python, negative indexes allow you to access elements of a sequence (like a list, string, or tuple) from the end instead of the beginning.
        [-1] → last element
        [-2] → second last element
        [-3] → third last element and so on

=>  They are used for beacuse:
    -  Easier access from the end
    -  Reduces extra variables or calculations
    -  It also works with slices

=>  Eg:'''
fruits = ["apple", "banana", "cherry", "dates"]
print(fruits[-1]) 
print(fruits[-2])