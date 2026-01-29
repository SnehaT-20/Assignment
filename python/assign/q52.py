'''How Do You Check the Presence of a Key in A Dictionary?'''

my_dict = {"name": "Sneha", "age": 22, "city": "Dwarka"}
if  my_dict.get("age") is not None:
    print("Key is present")
else:
    print("Key is not present")
