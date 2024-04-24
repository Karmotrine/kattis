import math

def get_circle_area(pi: float, r: float) -> float:
    return pi * (r * r)

# Monte-Carlo Method
def get_estimate_pi(inside: float, total:float) -> float:
    return 4.0 * (inside / total)

while (True):
    r, m, c = [float(x) for x in list(input().split())]
    if (r == 0 and m == 0 and c == 0):
        break
    real_area = get_circle_area(math.pi, r)
    estimate_pi = get_estimate_pi(c, m)
    estimate_area = get_circle_area(estimate_pi, r)
    print(f"{real_area:.8f} {estimate_area:.8f}")