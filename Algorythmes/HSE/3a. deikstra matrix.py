import heapq as hq
import math

N, S, F = map(int, input().split())

G = []

for i in range(N):
	G.append(list(map(int, input().split())))

# print(G[1])



def dijkstra(G, s):
	n = len(G)
	visited = [False]*n
	weights = [math.inf]*n
	path = [None]*n
	queue = []
	weights[s] = 0
	hq.heappush(queue, (0, s))
	while len(queue) > 0:
		g, u = hq.heappop(queue)
		visited[u] = True
		for v, w in G[u]:
			if not visited[v]:
				f = g + w
				if f < weights[v]:
					weights[v] = f
					path[v] = u
					hq.heappush(queue, (f, v))
	return path, weights

print(dijkstra(G, 0))