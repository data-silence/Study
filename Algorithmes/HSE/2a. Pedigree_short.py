def height(person):
	if person not in pedigree_dict:
		return 0
	else:
		return 1 + height(pedigree_dict[person])


pedigree_dict = {}
n = int(input())
for i in range(n - 1):
	child, parent = input().split()
	pedigree_dict[child] = parent

person_height_dict = {}
for man in set(pedigree_dict.keys()).union(set(pedigree_dict.values())):
	person_height_dict[man] = height(man)

for key, value in sorted(person_height_dict.items()):
	print(key, value)

