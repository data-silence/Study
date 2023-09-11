r = int(input())
i = int(input())
c = int(input())

if i == 6:
	res = 0
elif i == 7:
	res = 1
elif i == 1:
	res = c
elif i == 0 and r != 0:
	res = 3
elif i == 0 and r == 0:
	res = c
elif i == 4 and r != 0:
	res = 3
elif i == 4 and r == 0:
	res = 4
else:
	res = i

print(res)
