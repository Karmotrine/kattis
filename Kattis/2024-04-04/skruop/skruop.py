num = int(input())
volume = 7
for i in range(num):
    command = input().split(" ")
    if command[1] == "op!" and volume < 10:
        volume += 1
    elif command[1] == "ned!" and volume > 0:
        volume -= 1
        
print(volume)