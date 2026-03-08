'''Can one block of except statements handle multiple exception? 

=>  yes, we can handle multiple exception in one except statement block.
=>  You can do this by grouping multiple exception types inside parentheses.
=>  Syntax:
            try:
                # risky code
            except (Exception1, Exception2, Exception3):
                # handle all these exceptions here
=>  Example:
'''
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero error!")
