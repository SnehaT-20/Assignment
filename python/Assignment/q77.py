'''Write a Python program to read a file line by line store it into a variable.'''

with open("d:\\tops\\python\\writ.txt", "r") as file:
    content = file.read()
    file.close()
print(content)
