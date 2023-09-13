N, Source_node, Final_node = map(int, input().split())
Source_node -= 1
Final_node -= 1
graf_list = []

infinity = 10 ** 10
weight_matrix = [infinity] * N
weight_matrix[Source_node] = 0
boolean_matrix = [False] * N
road_matrix = [None] * N


for i in range(N):
    graf_list.append(list(map(int, input().split())))

while True:
    min_dist = infinity
    for i in range(N):
        if not boolean_matrix[i] and weight_matrix[i] < min_dist:
            min_dist = weight_matrix[i]
            min_vertex = i
    if min_dist == infinity:
        break
    i = min_vertex
    boolean_matrix[i] = True
    for j in range(N):
        if weight_matrix[i] + graf_list[i][j] < weight_matrix[j] and graf_list[i][j] != -1:
            weight_matrix[j] = weight_matrix[i] + graf_list[i][j]
            road_matrix[j] = i
if weight_matrix[Final_node] == infinity:
    print(-1)
else:
    path_list = []
    while Final_node is not None:
        path_list.append(Final_node + 1)
        Final_node = road_matrix[Final_node]
    print(" ".join(map(str, path_list[::-1])))
