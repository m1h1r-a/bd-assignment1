#!/usr/bin/env python3
import sys

'''
Sample Input:
request_id client_id endpoint timestamp no_of_servers_down  

request_id predicted_status_code

r001 c01 user/profile 00:00:00 2.0        #200 
r002 c02 user/profile 00:00:00 2.0        #500
r003 c03 user/settings 00:01:02           #200
r004 c01 order/history 00:01:05 2.0       #200
r005 c05 order/history 00:05:03 3.0       #500
r006 c03 order/history 00:05:03 3.0       #500
r007 c02 user/settings 00:07:00 1.0       #200
r008 c03 user/settings 00:07:05           #200
r009 c01 user/profile 00:08:00            #200
r010 c04 user/profile 00:08:05 3.0        #500

r001 500
r002 500
r003 200
r004 200
r005 500
r006 500
r007 200
r008 200
r009 500
r010 200
'''

for line in sys.stdin:
    data = line.split()
    
    for item in data:
        print(item,end=" ")
    print()










