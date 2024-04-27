num_servers = int(input())
inv = {"cpu": 0, "ram": 0, "hdd": 0}
for i in range(num_servers):
    cpu, ram, hdd = input().split()
    if cpu == "J": inv["cpu"] += 1
    if ram == "J": inv["ram"] += 1
    if hdd == "J": inv["hdd"] += 1

print(min(inv.values()))