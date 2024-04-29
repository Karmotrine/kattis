cols = int(input())
rows = int(input())
car_count = 0
space_count = 0
for i in range(rows):
    current_inp = input()
    for char in current_inp:
        if char == '#':
            car_count += 1
        else:
            space_count += 1

print(f"{float(space_count / (cols * rows))}")