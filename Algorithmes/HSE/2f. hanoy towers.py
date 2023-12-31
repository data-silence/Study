""" Данная программа находит решение головоломки Ханойская башня - находит способ перемещения дисков
из одного стержня на другой по определенным правилам и за наименьшее количество шагов """


# Суть программы-  напечатать для данного числа дисков n  последовательность перекладываний в формате n, x, y
# Условия: диски можно перекладывать с одного стержня на другой по одному, диск нельзя класть на диск меньшего диаметра

# n - количество дисков (в начале решения диски находятся на первом стержне)
# x — номер стержня с которого снимается диск, y — номер стержня на который он надевается.
# стержни пронумерованы 1,2,3, поэтому (6-x-y) - номер временного стержня,
#  через который в текущих условиях осуществляется перемещение башни из (n- 1) диска


def move(n, x=1, y=3):
	if n == 1:
		print(n, x, y)
	else:
		move(n - 1, x, 6 - x - y)
		print(n, x, y)
		move(n - 1, 6 - x - y, y)


disks_number = int(input())

move(disks_number)
