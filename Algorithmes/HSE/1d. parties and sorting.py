common_list = []
parties = []
votes = []
sort_list = {}


with open('input.txt', 'r') as file:
	for line in file.readlines():
		l = line.strip().strip('\n')
		if l != '':
			common_list.append(l)

parties = common_list[1:common_list.index('VOTES:')]
votes = common_list[common_list.index('VOTES:') + 1:]

for party in parties:
	sort_list[party] = votes.count(party)

sorted_tuple = sorted(sort_list.items(), key=lambda k: (-k[1], k[0]))

for party in sorted_tuple:
	print(party[0])
