#!/usr/bin/env python3
import sys

'''
Input: 
00:00:00 r001 100 c01 1.0 500 
00:00:00 r002 100 c02 1.0 500 
00:00:00 r020 200 c02 1.0 200 
00:01:02 r003 200 c03 3.0 200 
00:01:05 r004 300 c01 1.0 200 
00:05:03 r005 300 c05 0.0 500 
00:05:03 r006 300 c03 0.0 500 
00:07:00 r007 200 c02 2.0 200 
00:07:05 r008 200 c03 3.0 200 
00:08:00 r009 100 c01 3.0 500 
00:08:05 r010 100 c04 0.0 200 
'''

prevTime = ""
endpoints = {}
clients = {}
for line in sys.stdin:
    data = line.split()
    curTime = data[0]

    '''Calculate Actual Status Codes Logic:'''
    if prevTime == "" :
        prevTime = curTime
        clients.clear()
        clients[data[3]]=1
        endpoints.clear()
        endpoints[data[2]] = float(data[4])
        # print(f"here :{type(endpoints[data[2]])}")
        if endpoints[data[2]] > 0.0:
            data.append(200)
            endpoints[data[2]]-=1.0
        else:
            data.append(500)

    elif prevTime != curTime:
        prevTime = curTime
        clients.clear()
        clients[data[3]]=1
        endpoints.clear()
        endpoints[data[2]] = float(data[4])
        if endpoints[data[2]] > 0.0:
            data.append(200)
            endpoints[data[2]]-=1.0
        else:
            data.append(500)

    elif prevTime == curTime:

        if data[3] in clients:
            continue
        else:
            clients[data[3]]=1

        if data[2] not in endpoints:
            endpoints[data[2]] = float(data[4])

        if endpoints[data[2]] > 0.0:
            data.append(200)
            endpoints[data[2]]-=1.0
        else:
            data.append(500)

    if int(data[5]) == int(data[6]):
        data.append(1)
    else:
        data.append(0)
    

    #sort by client
    temp = data[1]
    data[1] = data[3]
    data[3] = temp


    del data[5]
    del data[4]
    del data[3]
    del data[0]
    
    for item in data:
        print(item,end=" ")
    print()

