def find_gcd(x, y):
    return (x if (y == 0) else find_gcd(y, x % y))
    
input_num = input().split()
print(find_gcd(int(input_num[0]), int(input_num[1])))