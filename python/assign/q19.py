'''Write a Python program to count the occurrences of each word in a given string'''
text = input("enter your string: ")
words = text.split()

for word in set(words):
    print(word, ":", words.count(word))
