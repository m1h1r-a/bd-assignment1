#!/usr/bin/env python3
import sys

'''
Input:
c01 100 200 0 
c04 600 200 0 
c06 300 500 1 
c08 700 500 1 
c03 600 200 0 
c10 100 200 1 
c01 900 200 1 
c02 700 200 0 
c03 500 200 1 
c06 900 500 1 
c07 900 500 1 
'''

for line in sys.stdin:
    data = line.split()

    # data[1] = int(data[1])
    # data[2] = int(data[2])
    # data[3] = int(data[3])

    for item in data:
        print(item,end=" ")
    print()


# # clients = {}
# prevClient = ""
# cost = 0
# count = 0
# succesfullPredictions = 0
# for line in sys.stdin:
#     data = line.split()
#     curClient = data[0]
#
#     data[1] = int(data[1])
#     data[2] = int(data[2])
#     data[3] = int(data[3])
#
#     # for item in data:
#     #     print(item,end=" ")
#     # print()
#
#     if prevClient == "":
#         prevClient = curClient
#         count+=1
#
#     elif prevClient!=curClient:
#         print(f"{prevClient} {succesfullPredictions} {count} {cost}")
#         prevClient = curClient
#         cost = 0
#         succesfullPredictions = 0
#         count = 1
#         if data[3] == 1:
#             succesfullPredictions+=1
#         if data[2] == 200:
#             cost+=data[1]
#
#     elif prevClient == curClient:
#         count+=1
#         if data[3] == 1:
#             succesfullPredictions+=1
#         if data[2] == 200:
#             cost+=data[1]
#
# print(f"{prevClient} {succesfullPredictions} {count} {cost}")
