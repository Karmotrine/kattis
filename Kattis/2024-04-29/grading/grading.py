marks = [int(x) for x in input().split()]
grade = int(input())

def determine_grade(thisGrade: int, marks: list) -> str:
    current_ptr = 0
    # A - D
    for i in range(len(marks)):
        if thisGrade >= marks[i]:
            return chr(65 + current_ptr)
        current_ptr += 1
    # F
    return "F"

print(determine_grade(grade, marks))