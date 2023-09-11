import math


d = int(input())
x, y = map(int, input().split())

angle_X = math.atan2(x, y)
hyp_X = (d*abs(math.sqrt(2)))/(2*math.cos(angle_X))
dl_X = abs(math.sqrt(x**2 + y**2))


def dist_dot(xa_coord, ya_coord, xb_coord, yb_coord):
    dist = abs(math.sqrt(((xb_coord-xa_coord)**2) + (yb_coord-ya_coord)**2))
    return dist


if hyp_X >= dl_X:
    res = 0
else:
    list_distances_to_dot = []
    list_distances_to_dot.append(dist_dot(0, 0, x, y))
    list_distances_to_dot.append(dist_dot(d, 0, x, y))
    list_distances_to_dot.append(dist_dot(0, d, x, y))
    shortest_dist = min(list_distances_to_dot)
    shortest_dot = list_distances_to_dot.index(shortest_dist)
    if shortest_dot == 0 or (list_distances_to_dot[0] == list_distances_to_dot[1]):
        res = 1
    elif shortest_dot == 1 or (list_distances_to_dot[1] == list_distances_to_dot[2]):
        res = 2
    else:
        res = 3
    print(list_distances_to_dot)

# print(d, x, y)
# print(angle_X, hyp_X, dl_X)

print(res)