cycles = int(input())
flags = []
for i in range(3):
    digits = [int(x) for x in input().split()]
    if 7 in digits:
        flags.append(7)

print(f"{777 if len(flags) == 3 else 0}")