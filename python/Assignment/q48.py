'''Write a Python script to sort (ascending and descending) a 
dictionary by value.'''

marks={'a':50,'b':60, 'c':40, 'd':70, 'e':90}
ascending = dict(sorted(marks.items(), key=lambda x: x[1]))
descending = dict(sorted(marks.items(), key=lambda x: x[1], reverse=True))
print(ascending)
print(descending)