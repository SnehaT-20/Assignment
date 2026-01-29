'''Write a Python function to check whether a number is in a given range'''
starting=int(input("Enter your start number: "))
ending=int(input("Enter your end number: "))
num=int(input("Enter your searching number: "))
def check_range(number, start, end):
    if start <= number <= end:
        print("Number is in the given range")
    else:
        print("Number is NOT in the given range")
check_range(num,starting,ending)

