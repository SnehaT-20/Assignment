'''Write a Python program to count the frequency of words in a file. '''
 
file = open("d:\\tops\\python\\Assignment\\text.txt", "r")
text = file.read()   
file.close()
words = text.split()
freq = {}
for i in words:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)