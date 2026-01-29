'''Write a Python function to insert a string in the middle of a string'''
s1=input("Enter your main string: ")
s2=input("Enter your string for insert: ")
half= len(s1)//2
ans=s1[:half]+s2+s1[half:]
print(ans)