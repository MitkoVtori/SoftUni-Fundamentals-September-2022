from math import floor

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())


def distance(_x1, _y1, _x2, _y2):
    return (_x2-_x1)**2 + (_y2-_y1)**2


x1y1 = distance(x1, y1, 0, 0)
x2y2 = distance(x2, y2, 0, 0)
x3y3 = distance(x3, y3, 0, 0)
x4y4 = distance(x4, y4, 0, 0)

line_1 = x1y1 + x2y2
line_2 = x3y3 + x4y4

if line_1 >= line_2:
    if x1y1 <= x2y2:
        print(f'({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})')
    else:
        print(f'({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})')
if line_1 < line_2:
    if x3y3 <= x4y4:
        print(f'({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})')
    else:
        print(f'({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})')