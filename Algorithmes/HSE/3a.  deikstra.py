N, S, F = map(int, input().split())
# N - количество вершин графа (количество городов - последующих строк в матрице смежности)
# S - начальная вершина графа (пункт отправления)
# F - конечная вершина графа (пункт назначения)

W = [] # промежуточный словарь для обработки матрицы смежностей

for i in range(N):
	W.append(list(map(int, input().split())))

distances = {}

for i in range(len(W)):
	temp = {}
	for j in range(len(W)):
		if j != i:
			temp[j+1] = W[i][j]
	distances[i + 1] = temp

# print(graf)

nodes = tuple(distances.keys())
# print(nodes)


# nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
# distances = {
#     'B': {'A': 5, 'D': 1, 'G': 2},
#     'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
#     'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
#     'G': {'B': 2, 'D': 1, 'C': 2},
#     'C': {'G': 2, 'E': 1, 'F': 16},
#     'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
#     'F': {'A': 5, 'E': 2, 'C': 16}}


unvisited = {node: None for node in nodes} #using None as +inf
visited = {}
current = S
currentDistance = 0
unvisited[current] = currentDistance

while True:
	for neighbour, distance in distances[current].items():
		if neighbour not in unvisited: continue
		newDistance = currentDistance + distance
		if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
			unvisited[neighbour] = newDistance
	visited[current] = currentDistance
	del unvisited[current]
	if not unvisited: break
	candidates = [node for node in unvisited.items() if node[1]]
	current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

print(visited)
