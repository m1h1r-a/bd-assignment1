#!/usr/bin/env python3
import sys

'''
Input:
c01 1000 200 0 
c01 1000 200 1 
c01 1000 200 1 
c01 100 200 0 
c01 100 200 0 
c01 100 200 0 
c01 200 200 0 
c01 200 200 1 
c01 200 200 1 
c01 200 500 0 
c01 200 500 0 
'''


# clients = {}
prevClient = ""
cost = 0
count = 0
succesfullPredictions = 0
for line in sys.stdin:
    data = line.split()
    curClient = data[0]

    data[1] = int(data[1])
    data[2] = int(data[2])
    data[3] = int(data[3])

    # for item in data:
    #     print(item,end=" ")
    # print()

    if prevClient == "":
        prevClient = curClient
        count = 1
        if data[3] == 1:
            succesfullPredictions+=1
        if data[2] == 200:
            cost+=data[1]

        
    elif prevClient!=curClient:
        print(f"{prevClient} {succesfullPredictions}/{count} {cost}")
        prevClient = curClient
        cost = 0
        succesfullPredictions = 0
        count = 1
        if data[3] == 1:
            succesfullPredictions+=1
        if data[2] == 200:
            cost+=data[1]
    
    elif prevClient == curClient:
        count+=1
        if data[3] == 1:
            succesfullPredictions+=1
        if data[2] == 200:
            cost+=data[1]

print(f"{prevClient} {succesfullPredictions}/{count} {cost}")



# print(f"{data[0]} {data[1]}/{data[2]} {data[3]}")
