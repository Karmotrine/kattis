def check(n1: int, n2: int, res: int) -> bool:
    if n1 + n2 == res: return True
    if n1 - n2 == res or n2 - n1 == res: return True
    if n1 * n2 == res : return True
    if n1 / n2 == float(res) or n2 / n1 == float(res): return True
    return False

cycles = int(input())
for i in range(cycles):
    inp = [int(x) for x in list(input().split())]
    n1 = inp[0]
    n2 = inp[1]
    n3 = inp[2]
    print(f'{"Possible" if check(n1, n2, n3) else "Impossible"}')