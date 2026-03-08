'''Write python program that user to enter only odd numbers, else 
will raise an exception'''
try:
    num = int(input("Enter an odd number: "))    
    if num % 2 == 0:
        raise Exception("Its an even number! Please enter an odd number.")
    else:
        print(f"Thank you! {num} is an odd number.")    
except Exception as e:
    print(e)