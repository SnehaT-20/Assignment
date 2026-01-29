'''Write a Python function that checks whether a passed string is 
palindrome or not'''
string=input("Enter your string: ")
def is_palindrome(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    if s == reversed_s:
        return "True"
    else:
        return "False"
print(is_palindrome(string))
