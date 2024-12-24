#!/usr/bin/env python3
import sys
import json

'''
Sample Input: 

Ahmedabad loss
Ahmedabad loss
Ahmedabad loss
Ahmedabad loss
Ahmedabad loss
Ahmedabad loss
Ahmedabad profit
Ahmedabad profit
Ahmedabad profit
Bangalore loss
Bangalore loss
Bangalore loss
Bangalore loss
Bangalore profit
Bangalore profit
Bangalore profit
Bangalore profit
Bangalore profit
'''

'''Output: {"city": "Bangalore", "profit_stores": 2, "loss_stores": 0}'''

prevCity = ""
profit_count = 0
loss_count = 0
for line in sys.stdin:
    data_list = line.split()
    curCity = data_list[0]

    if prevCity=="":
        prevCity = curCity
        # print(f"Running here for: {prevCity}")
        profit_count = 0
        loss_count = 0
        if data_list[1] == "profit":
            profit_count+=1
        else:
            loss_count+=1

    elif curCity != prevCity:
        #print prevCity values:
        # print(f"changed from: {prevCity} to {curCity}")
        print(f'{{"city": "{prevCity}", "profit_stores": {profit_count}, "loss_stores": {loss_count}}}')

        #change update values
        prevCity = curCity
        profit_count = 0
        loss_count = 0
        if data_list[1] == "profit":
            profit_count+=1
        else:
            loss_count+=1

    elif curCity==prevCity: #CurStore == prevStore
        if data_list[1] == "profit":
            profit_count+=1
        else:
            loss_count+=1

    #for last city:
print(f'{{"city": "{prevCity}", "profit_stores": {profit_count}, "loss_stores": {loss_count}}}')





