d = int(input())
x, y = map(int, input().split())
res = 0

if (x + y) <= d:
    res = 0

elif x < 0 and y < 0:
    res = 1

elif x >= 0 and y >= 0:
    if x >= y:
        res = 2
    else:
        res = 3

elif x > 0 > y:
    if x <= d / 2:
        res = 1
    else:
        res = 2

elif y > 0 > x:
    if y <= d / 2:
        res = 1
    else:
        res = 3

print(res)
