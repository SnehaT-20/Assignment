'''Write a Python program to map two lists into a dictionary 
Sample output: Counter ({'a': 400, 'b': 400,'d': 400, 'c': 300})'''

keys=['a','b','d','c']
values=[400,400,400,300]
ans=dict(zip(keys,values))
print(ans)
