#!/usr/bin/env python3
import sys
import json

'''
sample json:
{
  "city": "Bangalore",
  "store_id": "ST01293",
  "categories": [
    "Electronics",
    "Groceries"
  ],
  "sales_data": {
    "Electronics": {
      "revenue": 600000,
      "cogs": 500000
    },
    "Groceries": {
      "revenue": 250000,
      "cogs": 270000
    }
  }
}
'''

''' in sales data, salesdata keys should be present in the categories array
 if salesdata keys not in catagory array, ignore the store_id'''

# input = sys.stdin.read()
# listData = json.loads(input)
# for data in listData:

for line in sys.stdin:
    line = line.strip()
    # print(f"before: {line}")
    if line[0]=='[' or line[0]==']':
        continue;
    line  = line.strip(',')
    # print(f"after: {line}")

    '''This is for each json object(each store) as an item in the list'''
    data = json.loads(line)
    # print(type(data))
    # print(data)
    # for i in range(2):
    #     print()
    city = data.get('city')
    store_id = data.get('store_id')
    categories = data.get('categories')
    sales_data = data.get('sales_data')
    tempRevenue = 0 
    tempCogs = 0 

    sales_keys = sales_data.keys()
    # print(categories)
    dep_count = 0
    for dept in categories:
        if dept in sales_keys:
            '''For each department that we have data access to'''
            # print(store_id)
            try:
                tempRevenue+=sales_data[dept]["revenue"]
            except:
                continue
            try:
                tempCogs+=sales_data[dept]["cogs"]
            except:
                tempRevenue-=sales_data[dept]["revenue"]
                continue
            dep_count+=1
                
    if dep_count > 0:
        if(tempRevenue>tempCogs):
            print(f"{city} profit {store_id}")
        else:
            print(f"{city} loss {store_id}")
    else:
        continue


    # print(keys)
    # for key in sales_keys:
    #     print(f"{sales_data[sales_keys]}")
