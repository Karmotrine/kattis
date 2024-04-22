input_num = int(input())
toktikers = {}
for i in range(input_num):
    line = input().split()
    name = line[0]
    views = int(line[1])
    if name in toktikers.keys():
        toktikers[name] = toktikers[name] + views
    else:
        toktikers[name] = views

print(max(toktikers, key=toktikers.get))