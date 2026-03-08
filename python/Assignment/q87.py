'''When is the finally block executed?

=>  The finally block is always executed whether an exception occurs or no exception occurs.
=>  The finally block is executed every time.
=>  Example:
'''
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Finally block executed")