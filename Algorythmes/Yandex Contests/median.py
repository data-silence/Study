s = int(input())
l = list(map(int, input().split()))
if s%2 == 0:
	print(int(s/2))
else:
	print(len(l))
	print(s/len(l))


	for el in range(10):
		print el