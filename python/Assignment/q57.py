'''Write a Python program to find the highest 3 values in a dictionary'''
dict1={"a":20,"b":11,"c":24,"d":10,"e":50,"f":90}
values = sorted(dict1.values(), reverse=True)
highest = values[:3]
print(highest)