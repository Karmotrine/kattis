master_list = {}
cycle = int(input())
for i in range(cycle):
    name, priority, date = input().split()
    if date in master_list:
        if int(priority) > master_list[date]["priority"]:
            master_list[date] = {
                "name" : name,
                "priority": int(priority)
            }
        else:
            continue
    else:
        master_list[date] = {
            "name": name,
            "priority": int(priority)
        }
sorted_list = dict(sorted(master_list.items(), key= lambda x: x[1]['name']))
print(len(sorted_list.items()))
for k,v in sorted_list.items():
    print(v['name'])