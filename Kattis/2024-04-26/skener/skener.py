def transform(row: str, zr: int, zc: int) -> str:
    local_output = ""
    for i in range(zr):
        column_transform_output = ""
        for char in row:
            for i in range(zc):
                column_transform_output += char
        local_output += column_transform_output + '\n'
    return local_output

r, c, zr, zc = [int(x) for x in list(input().split())]
global_output = ""
for i in range(r):
    this_row = input()
    global_output += transform(this_row, zr, zc)
print(global_output)