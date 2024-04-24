inp = input()

def product(string_input: str) -> int:
    positive_input_array = [int(x) for x in list(string_input) if int(x) > 0]
    product = 1
    for current_number in positive_input_array:
        product *= current_number
        
    return str(product)

def get_digitproduct(string_input: str) -> int:
    if len(string_input) == 1:
        return string_input
    else:
        return get_digitproduct(product(string_input))
        
print(get_digitproduct(inp))