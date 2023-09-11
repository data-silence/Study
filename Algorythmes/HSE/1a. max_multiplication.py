l = list(map(int, input().split()))

diff = 0

if len(l) == 2:
	if l[0] <= l[1]:
		print(l[0], l[1])
	else:
		print(l[-1], l[-2])

if len(l) == 3:
	if 0 in l:
		l.remove(0)
	if sorted(l)[1] > 0:
		print(sorted(l)[-2], sorted(l)[-1])
	else:
		print(sorted(l)[0], sorted(l)[1])

if len(l) >= 4:
	l_max1 = l.pop(l.index(max(l)))
	l_max2 = l.pop(l.index(max(l)))
	l_min1 = l.pop(l.index(min(l)))
	l_min2 = l.pop(l.index(min(l)))

	diff = l_max1 * l_max2 - l_min1 * l_min2

	if diff > 0:
		print(l_max2, l_max1)
	else:
		print(l_min1, l_min2)
