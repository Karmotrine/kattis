n1, n2, n3 = 1, 2, 3
count = 0
prod = 1
inp = int(input())
while True:
    prod = n1*n2*n3
    if prod >= inp:
        break
    n1 += 1
    n2 += 1
    n3 += 1
    count += 1
print(count)