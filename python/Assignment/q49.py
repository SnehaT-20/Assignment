'''Write a Python script to concatenate following dictionaries to create 
a new one.'''
dict1={'sneha':5646, 'mona':9856, 'mohnish':8523}
dict2={'nitin':5214}
dict3={'parth':9513, 'samarth':2034}
new_dict={}
new_dict.update(dict1)
new_dict.update(dict2)
new_dict.update(dict3)
print(new_dict)