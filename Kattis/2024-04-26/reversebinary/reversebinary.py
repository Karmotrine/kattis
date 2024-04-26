inp = int(input())
reverse_inp = int("".join(list(reversed(str(bin(inp))))[:-2]), 2)
print(reverse_inp)