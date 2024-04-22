cycles = int(input())
for i in range(cycles):
    num_guests = input()
    guests = input().split()
    unique = [e for e in guests if guests.count(e) == 1]
    print(f'Case #{i + 1}: {unique[0]}')
    continue