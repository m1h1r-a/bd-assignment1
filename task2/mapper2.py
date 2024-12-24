#!/usr/bin/env python3
import sys

'''
Input:

00:00:53 c01 900 r001 3.0 500 
00:01:25 c09 900 r002 3.0 500 
00:00:45 c02 700 r003 3.0 500 
00:01:53 c01 700 r004 3.0 200 
00:00:56 c07 900 r005 1.0 500 
00:01:16 c04 600 r006 3.0 500 
00:00:46 c01 1000 r007 1.0 200 
00:01:34 c05 700 r008 0.0 200 
00:00:28 c08 400 r009 0.0 500 
00:01:42 c07 500 r010 1.0 200 
00:01:31 c03 600 r011 2.0 500 
00:00:17 c06 300 r012 1.0 500 
00:00:25 c03 700 r013 0.0 500 
'''

# prevTime = ""
# endpoints = {}
for line in sys.stdin:
    data = line.split()


    #change to find no. of available_servers
    data[4] = 3.0 - float(data[4])

    #lexicographic ordering of requests
    temp = data[1]
    data[1] = data[3]
    data[3] = temp

    # curTime = data[0]
    # #change to find no. of available_servers
    # data[4] = 3.0 - float(data[4])

    # '''Calculate Actual Status Codes Logic:'''
    # if prevTime == "" :
    #     prevTime = curTime
    #     endpoints.clear()
    #     endpoints[data[2]] = data[4]
    #     if endpoints[data[2]] > 0.0:
    #         data.append(200)
    #         endpoints[data[2]]-=1.0
    #     else:
    #         data.append(500)
    #
    # elif prevTime != curTime:
    #     prevTime = curTime
    #     endpoints.clear()
    #     endpoints[data[2]] = data[4]
    #     if endpoints[data[2]] > 0.0:
    #         data.append(200)
    #         endpoints[data[2]]-=1.0
    #     else:
    #         data.append(500)
    #
    # elif prevTime == curTime:
    #     if data[2] not in endpoints:
    #         endpoints[data[2]] = data[4]
    #
    #     if endpoints[data[2]] > 0.0:
    #         data.append(200)
    #         endpoints[data[2]]-=1.0
    #     else:
    #         data.append(500)
    # del data[0]


    for item in data:
        print(item,end=" ")
    print()
