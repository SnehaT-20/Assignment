'''How can you pick a random item from a list or tuple?'''

import random
my_list = [10, 20, 30, 40, 50]
my_tuple = ('a', 'b', 'c', 'd') 
print("Random from list:", random.choice(my_list))
print("Random from tuple:", random.choice(my_tuple))