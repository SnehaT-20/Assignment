'''Write a Python program to read first n lines of a file.'''

with open("d:\\tops\\python\\writ.txt", "r") as file:
    n = int(input("Enter number of lines: "))
    for i in range(n):
        print(file.readline(), end="")
