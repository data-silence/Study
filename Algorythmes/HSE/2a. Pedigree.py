n = int(input())

p_tree = {}  # это будет словарь {ребёнок=родитель}

# создаём словарь p_tree
for _ in range(1, n):  # читаем строки
    line = input()
    child, parent = line.split()  # ребёнок,родитель = 'str1 str2'.split()
    p_tree[child] = parent  # p_tree[ребёнок]='родитель'

# all_man = множество, все люди
all_man = set(p_tree.keys()) | set(p_tree.values())  # (все имена в единственном числе) = (все родители) + (все дети)

heights = {}  # будет словарь {предок=поколение}


# вычисляет поколение, попутно создаёт словарь, чтоб не вычислять одно и тоже
def f(name):  # передаём имя
    if name not in p_tree:  # если нет родителя
        heights[name] = 0  # предок = 0,запись в словарь heights
        return 0  # значение поколения для дальнейшего вычисления
    parent = p_tree[name]  # родитель = смотрим в (ребёнок=родитель)
    if parent in heights:  # если известно поколение родителя
        value = heights[parent] + 1  # поколение = (поколение родителя)+1
    else:
        value = f(
            parent) + 1  # поколение = поколение родителя +1, имя родителя отдаём функции, она вернёт поколение родителя
    heights[name] = value  # добавляем в словарь heights нового предка [имя] = поколение
    return value  # значение поколения для дальнейшего вычисления


# создадим словарь (предок=поколение)
for name in all_man:  # возьмем всех по очереди
    if name not in heights:  # берём только тех, кого нет в словаре (предок=поколение)
        f(name)  # дать имени поколение попутно создавая словарь (предок-поколение)

# for name in sorted(heights):
#     print(name, heights[name])

print(p_tree)
print(all_man)
print(heights)