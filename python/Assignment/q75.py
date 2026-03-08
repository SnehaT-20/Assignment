'''Write a Python program to read last n lines of a file. '''

with open("d:\\tops\\python\\writ.txt", "r") as file:
    n = int(input("Enter number of lines: "))
    for i in file.readlines[-n:]:
        print(i, end="")