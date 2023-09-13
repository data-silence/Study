result = 0

tariffs = sorted(list(map(int, input().split())))
distances = sorted(list(map(int, input().split())), reverse=True)
zipped_pairs = zip(tariffs, distances)

for pair in zipped_pairs:
	result += pair[0] * pair[1]
print(result)
