cycles = int(input())
for i in range(cycles):
    length, *grades = [float(x) for x in input().split()]
    avg = sum(grades) / len(grades)
    num_passers = len(list(filter(lambda x: (float(x) > avg), grades)))
    passing_rate = num_passers / len(grades) * 100
    print("{:.3f}".format(passing_rate) + "%")