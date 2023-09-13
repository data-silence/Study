input_file = open("input.txt", "r")
output_file = open("output.txt", "w")
infinity = 10 ** 9
a = []
b = []
c = []
d = []

N = int(input())
Source_node, Final_node = map(int, input().split())
R = int(input())

for i in range(R):
    line = list(map(int, input().split()))
    a.append(int(line[0]))
    b.append(int(line[1]))
    c.append(int(line[2]))
    d.append(int(line[3]))

distination = []
for i in range(N):
    distination.append(infinity)

distination[Source_node - 1] = 0
for i in range(N - 1):
    for j in range(R):
        if distination[c[j] - 1] > d[j] and distination[a[j] - 1] != infinity and b[j] >= distination[a[j] - 1]:
            distination[c[j] - 1] = d[j]

for i in range(N):
    if distination[i] == infinity:
        distination[i] = 0

for i in range(N):
    if distination[i] == 0:
        distination[i] = -1
        distination[Source_node - 1] = 0

result_time = distination[Final_node - 1]
print(result_time)
