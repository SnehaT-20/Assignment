'''When will the else part of try-except-else be executed ?

=>  The else part of a try-except-else block is executed when no exception occurs in the try block.
=>  If the try block runs successfully then else block executes.
=>  If an exception occurs in try then except block executes and else is skipped.
=>  Example:
'''
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division successful!")
