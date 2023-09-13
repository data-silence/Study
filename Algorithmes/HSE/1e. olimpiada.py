result = {}

with open('input.txt', 'r') as file:
	for line in file.readlines()[1:]:
		l = line.strip().strip('\n').split()
		if l != '':
			result[l[0]] = int(l[1])

# print(result)
sorted_tuple = sorted(result.items(), key=lambda k: (-k[1], k[0]))

for values in sorted_tuple:
	print(values[0])
