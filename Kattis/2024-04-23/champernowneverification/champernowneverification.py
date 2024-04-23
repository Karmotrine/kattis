inp = input()
ran = list(range(int(inp[len(inp) - 1])))
expected = "".join([str(i + 1) for i in ran])
result = inp[len(inp) - 1] if expected == inp else -1
print(result)
