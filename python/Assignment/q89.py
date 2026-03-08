'''How Do You Handle Exceptions with Try/Except/Finally in Python? 
Explain with coding snippets. 

=> Exception handling in Python is done using:
       -  try → Code that may cause an error
       -  except → Handles the error
       -  finally → Always executes (cleanup block)
=> In below example, first Try block will execute. It contain normal program. It may contain error.
=> In try block num1 is divided with num2 means 10/0 which is not possible and this type of error is knowns as
    ZeroDivisionError.
=> So to handle this error without crashing the program we used Exception block.
=> Here we used ZeroDivisionError exception to handle this specific error.
=> After executing exception, Finally block is executed.
=> Finally block is executed whether exception is execute or not.
'''
try:
    num1 = 10
    num2 = 0
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution completed.")