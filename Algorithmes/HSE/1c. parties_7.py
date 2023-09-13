common_list = []
parties = []
votes = []

with open('input.txt', 'r') as file:
	for line in file.readlines():
		l = line.strip().strip('\n')
		if l != '':
			common_list.append(l)

while '' in common_list:
	common_list.remove('')

parties = common_list[1:common_list.index('VOTES:')]
votes = common_list[common_list.index('VOTES:') + 1:]

for party in parties:
	if votes.count(party) * 100 // len(votes) >= 7:
		print(party)
