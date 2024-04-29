def check_study(this_date: str) -> bool:
    year, month, day = this_date.split('/')
    return (int(year) >= 2010)

def check_birth(this_date: str) -> bool:
    year, month, day = this_date.split('/')
    return (int(year) >= 1991)

cycle = int(input())
for i in range(cycle):
    name, study_date, birth_date, courses = input().split()
    if (check_study(study_date)):
        print(f"{name} eligible")
    elif (check_birth(birth_date)):
        print(f"{name} eligible")
    elif (int(courses) < 41):
        print(f"{name} coach petitions")
    else:
        print(f"{name} ineligible")