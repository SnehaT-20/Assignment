'''Write a Python program to test whether a passed letter is a vowel 
or not.'''
letter = input("Enter your letter: ")
if letter in "AEIOUaeiou":
    print(f"Your given letter {letter} is:= Vowel")
else:
    print("Your given letter {letter} is:= not vowel")