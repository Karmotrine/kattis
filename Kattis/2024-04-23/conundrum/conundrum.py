name = "PER"
code = input()
change = 0
for i in range(0, len(code) - 1, 3):
    subset = code[i:i+3]
    for j in range(len(subset)):
        if subset[j] != name[j]:
            change += 1
            
print(change)