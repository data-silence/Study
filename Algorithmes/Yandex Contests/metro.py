N, i, j = map(int, input().split())
m = abs(j-i)
if m <= N/2:
	res = m-1
else:
	res = N-m-1
print(res)

