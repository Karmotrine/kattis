def check_harshad(x: int) -> bool:
    divisor = sum([int(i) for i in str(x)])
    return (x % divisor) == 0

target_num = int(input())
while(True):
    if check_harshad(target_num):
        print(target_num)
        break
    else:
        target_num += 1