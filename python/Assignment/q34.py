'''Write a Python function that takes two lists and returns true if they 
have at least one common member.'''

def comman(lst1, lst2):
    for i in lst1:
        if i in lst2:
            return True
    return False        
l1=[11,20,24,1,90]
l2=[90,20,11,1,24]
print(comman(l1,l2))


