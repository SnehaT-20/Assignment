'''Write a Python program to get the Fibonacci series of given range.'''

n = int(input("Enter the number of terms: "))
a = 0
b = 1
temp=0
print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    temp = a
    a = b
    b = temp + b
