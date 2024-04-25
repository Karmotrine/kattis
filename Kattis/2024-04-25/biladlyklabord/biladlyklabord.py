inp = input()
res = inp[0]
for i in range(len(inp)):
    if i > 0:
        if inp[i - 1] != inp[i]:
            res += inp[i]
print(res)