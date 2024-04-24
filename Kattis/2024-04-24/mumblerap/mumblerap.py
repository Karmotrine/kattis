letters = int(input())
mumble = input()
highest_digit = 0
digit = ""

for i in range(letters):
    if mumble[i].isnumeric():
        digit += mumble[i]
        if i == letters - 1:
            if int(digit) > highest_digit:
                highest_digit = digit
            digit = ""
    else:
        if len(digit) > 0:
            if int(digit) > highest_digit:
                highest_digit = int(digit)
            digit = ""
            
print(highest_digit)