'''Write a python program to sum of the first n positive integers.'''

n = int(input("Enter Your number := "))
sum = 0
for i in range(1, n+1):
    sum += i
    print(f"Your first n positive integer sum is := {sum}")
