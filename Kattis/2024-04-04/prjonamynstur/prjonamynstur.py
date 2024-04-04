LOOP_TO_MM = {
    "." : 20,
    "O" : 10,
    "\\": 25,
    "/": 25,
    "A": 35,
    "^": 5,
    "v": 22
}
input_str = input().split(' ')
row = int(input_str[0])

total_mm = 0

for r in range(row):
    current_row = input()
    for symbol in current_row:
        total_mm += LOOP_TO_MM[symbol]
        
print(total_mm)