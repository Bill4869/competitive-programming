import math

n = int(input())


def calRadius(p1, p2):
    diameter = pow(pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2), 1/2)
    return diameter / 2

def getCenter(p1, p2, radius):
    x = 0
    y = 0
    if(p1[0] < p2[0]):
        x = p1[0] + radius
    else:
        x = p1[0] - radius

    if(p1[1] < p2[1]):
        y = p1[1] + radius
    else:
        y = p1[1] - radius

    return x, y
x0, y0 = map(int, input().split())

x_h, y_h = map(int, input().split())

radius = calRadius((x0, y0), (x_h, y_h))

angle = 2 * math.pi / n

center_x, center_y = getCenter((x0, y0), (x_h, y_h), radius)



for i in range(n):
    print(center_x + radius * math.cos(2 * math.pi * i / n), center_y + radius * math.sin(2 * math.pi * i / n))

