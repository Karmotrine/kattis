def check_sauron(thisInput:str) -> str:
    left_side = thisInput.split("(")[0]
    right_side = thisInput.split(")")[1]
    if len(left_side) == len(right_side):
        return "correct"
    else:
        return "fix"
    
problem_input = input()
print(check_sauron(problem_input))