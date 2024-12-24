#!/usr/bin/env python3
import sys

'''
Sample Input From Mapper:

r001 500 
r001 c01 payment/submit 00:00:53 3.0 
r002 500 
r002 c09 payment/submit 00:01:25 3.0 
r003 500 
r003 c02 cart/add 00:00:45 3.0 
r004 200 
r004 c01 cart/add 00:01:53 3.0 
r005 500 
r005 c07 payment/submit 00:00:56 1.0 
'''

cost = {
    'user/profile': 100,
    'user/settings': 200,
    'order/history': 300,
    'order/checkout': 400,
    'product/details': 500,
    'product/search': 600,
    'cart/add': 700,
    'cart/remove': 800,
    'payment/submit': 900,
    'support/ticket': 1000
}

predVal = 0
for line in sys.stdin:
    data = line.split()

    if len(data) == 2:
        predVal = data[1]

    elif len(data) == 5:
        data.append(predVal)
        
        #replace endpoint with endpoint price
        try:
            data[2] = cost[data[2]]
        except:
            continue 

        #sort by time
        temp = data[0]
        data[0] = data[3]
        data[3] = temp

        for item in data:
            print(item,end=" ")
        print()

    elif len(data) == 4:
        data.append(0.0)
        data.append(predVal)

        #replace endpoint with endpoint price
        try:
            data[2] = cost[data[2]]
        except:
            continue 

        #sor by time
        temp = data[0]
        data[0] = data[3]
        data[3] = temp

        for item in data:
            print(item,end=" ")
        print()





