import math


def get_distance(_x1, _y1, _x2, _y2):
    return math.sqrt(math.pow(_x2 - _x1, 2.0) + math.pow(_y2 - _y1, 2.0))


x1 = math.floor(float(input()))
y1 = math.floor(float(input()))
x2 = math.floor(float(input()))
y2 = math.floor(float(input()))

dist1 = get_distance(x1, y1, 0, 0)
dist2 = get_distance(x2, y2, 0, 0)

if dist1 <= dist2:
    print(f"({x1}, {y1})")
else:
    print(f"({x2}, {y2})")