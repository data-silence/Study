"""Данная программа доказывает теорему Лагранжа - раскладывает простое нат.число по сумме квадртов нат.чисел не >4"""

lagrange_base = []  # здесь храним список оснований квадратов, по которым раскладывается искомое число


def lagrange(number, base):
	if number == 0:
		return lagrange_base.append(number)
	else:
		lagrange_base.append(base)
	if number == base ** 2:
		return lagrange_base
	# если функция не находит за один проход единственную базу, которая является полным решением,
	# то она запускается рекурсивно,при этом используя в качестве числа остаток после использования первой базы,
	# а новая база вычисляется заново
	remains = number - base ** 2
	new_base = int((remains ** 0.5) // 1)
	lagrange(remains, new_base)


start = int(input())
max_base = int((start ** 0.5) // 1)  # это первое число разложения - максимально возможная база разложения
# если в ходе выполнения функции с этой базой выясняется, что при её использовании получается больше 4 баз разложения -
# приходится уменьшать эту базу на единицу, что как раз и делается в цикле While ниже

result = lagrange(start, max_base)

while len(lagrange_base) > 4:
	lagrange_base = []
	max_base -= 1
	result = lagrange(start, max_base)

print(" ".join(map(str, lagrange_base)))
