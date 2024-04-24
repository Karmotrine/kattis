def hour_to_min(hr: int, minute: int):
    return hr * 60 + minute
    
def min_to_hour(thisMin: int):
    hr = (thisMin // 60) % 24
    minute = round(((thisMin / 60) - (thisMin // 60)) * 60)
    return f"{hr} {minute}"

hr, minute = [int(x) for x in list(input().split())]
input_tominute = hour_to_min(hr, minute)
print(min_to_hour(input_tominute - 45))