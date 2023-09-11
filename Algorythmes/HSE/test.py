N = int(input())
Source_node, Final_node = map(int, input().split())
R = int(input())
graf_list = []

for i in range(R):
    str = list(map(int, input().split()))
    str[1] = str[3] - str[1]
    str.pop(3)
    graf_list.append(str)

print(graf_list)

# Создаём матрицу с нулевой диагональю, и остальными элементами = -1
matrix = [[-1] * R for i in range(R)]
for i in range(R):
    matrix[i][i] = 0

    matrix[graf_list[i][0]][graf_list[i][2]] = graf_list[i][1]
    matrix[graf_list[i][2]][graf_list[i][0]] = matrix[graf_list[i][0]][graf_list[i][2]]

print(matrix)
# print(matrix)

# for el in graf_list:


for string in matrix:
    print(*string)


#
#
# # print(graf_list)
# print(matrix)
#
# spisok = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#


# print(matrix)
