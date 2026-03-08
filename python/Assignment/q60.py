'''Sample string:
 'w3resource' Expected output:
• {'3': 1,'s': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}'''
string=input("Enter your string: ")
dict1={}
for ch in string:
    if ch in dict1:
        dict1[ch] += 1
    else:
        dict1[ch] = 1
print(dict1)