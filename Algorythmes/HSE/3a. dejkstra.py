N, Source_node, Final_node = map(int, input().split())
Source_node -= 1
Final_node -= 1
graf_list = []

for i in range(N):
    graf_list.append(list(map(int, input().split())))
infinity = 10 ** 10
weight_matrix = [infinity] * N
weight_matrix[Source_node] = 0
boolean_matrix = [False] * N

while True:
    min_distance = infinity
    for i in range(N):
        if not boolean_matrix[i] and weight_matrix[i] < min_distance:
            min_distance = weight_matrix[i]
            min_vertex = i
    if min_distance == infinity:
        break
    i = min_vertex
    boolean_matrix[i] = True
    for j in range(N):
        if weight_matrix[i] + graf_list[i][j] < weight_matrix[j] and graf_list[i][j] != -1:
            weight_matrix[j] = weight_matrix[i] + graf_list[i][j]

if weight_matrix[Final_node] == infinity:
    print(-1)
else:
    print(weight_matrix[Final_node])

# print(weight_matrix)
# print(boolean_matrix)
