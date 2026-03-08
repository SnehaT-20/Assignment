'''Write a Python program to append text to a file and display the text. '''

with open("d:\\tops\\python\\writ.txt", "a") as file:
    file.write("\nThis text is appended.")

with open("d:\\tops\\python\\writ.txt", "r") as file:
    print(file.read())