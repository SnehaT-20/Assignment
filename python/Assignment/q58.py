'''Write a Python program to combine values in python list of dictionaries. 
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
300}, o {'item': 'item1', 'amount': 750}] 
Expected Output:
• Counter ({'item1': 1150, 'item2': 300})'''
data=[
{"Elecronics":"TV","amount":12000},
{"Elecronics":"Fridge","amount":10000},
{"Elecronics":"TV","amount":13000},
{"Elecronics":"Fridge","amount":4500},
{"Elecronics":"TV","amount":13000},
{"Elecronics":"AC","amount":25000},
{"Elecronics":"Home Theater","amount":30000}
]

# print(data[0])
# print(data[0]['Elecronics'])
# print(data[1]['Elecronics'],data[1]['amount'])
# print(data[2]['Elecronics'])

# print(data[0].keys())
lst_item=[]
for i in range(len(data)):
    #print(data[i]['Elecronics'])
    if data[i]['Elecronics'] not in lst_item:
        lst_item.append(data[i]['Elecronics'])

total_amount=0
dict_count={}
for item in range(len(lst_item)):
    total_amount=0
    for i in range(len(data)):
        if data[i]['Elecronics']==lst_item[item]:
         #   print(data[i]['Elecronics'] , lst_item[item] , data[i]['amount'])
            total_amount+=data[i]['amount']
            dict_count[data[i]['Elecronics']]=total_amount

print('Final ans',dict_count)
        

