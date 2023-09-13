N, S, F = map(int, input().split())
# N - количество вершин графа (количество городов - последующих строк в матрице смежности)
# S - начальная вершина графа (пункт отправления)
# F - конечная вершина графа (пункт назначения)
S -= 1
F -= 1
W = []

# считываем и записываем матрицу смежностей
for i in range(N):
    W.append(list(map(int, input().split())))
INF = 10 ** 10
D = [INF] * N
D[S] = 0
Colored = [False] * N
while True:
    min_dist = INF
    for i in range(N):
        if not Colored[i] and D[i] < min_dist:
            min_dist = D[i]
            min_vertex = i
        if min_dist == INF:
            break
        i = min_vertex
        Colored[i] = True
        for j in range(N):
            if D[i] + W[i][j] < D[j] and W[i][j] != -1:
                D[j] = D[i] + W[i][j]

        if D[F] == INF:
            print(-1)
        else:
            print(D[F])
