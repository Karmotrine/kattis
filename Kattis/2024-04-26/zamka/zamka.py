def minimal(mn: int, mx: int, sm: int) -> int:
    for i in range(mn, mx+1):
        if sum([int(x) for x in list(str(i))]) == sm:
            return i

def maximal(mn: int, mx: int, sm: int) -> int:
    for i in range(mx, mn-1, -1):
        if sum([int(x) for x in list(str(i))]) == sm:
            return i
            
L = int(input())
D = int(input())
X = int(input())
print(minimal(L,D,X))
print(maximal(L,D,X))