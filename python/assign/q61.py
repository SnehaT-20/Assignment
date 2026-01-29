'''Write a Python function to calculate the factorial of a number (a 
non-negative integer)'''
num = int(input("Enter a number: "))
def factorial(n):
    if n >= 0:
        result = 1
        for i in range(1, n + 1):
            result *= i
    return result
ans=factorial(num)
print(f"factorial is: {ans}")

 

 