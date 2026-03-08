'''Write a Python program to copy the contents of a file to another file. 
'''
with open("d:\\tops\\python\\writ.txt", "r") as file:
     data=file.read()  
     with open("write.txt","w") as file1:
        file1.write(data)
    