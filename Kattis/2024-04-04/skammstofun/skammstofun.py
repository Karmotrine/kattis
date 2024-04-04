num = int(input())
name = input().split(' ')
output = ""
for word in name:
    output += (word[0] if word[0].isupper() else "")
print(output)