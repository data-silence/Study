def dijkstra(graph, src, dest, visited=[], distances={}, predecessors={}):
    """ Вычисляет самый короткий путь между двумя заданными точками графа """
    # Несколько технических проверок на адекватность условий ввода
    if src not in graph:
        # raise TypeError('Корень дерева кратчайших путей не может быть найден')
        print(-1)
    if dest not in graph:
        # raise TypeError('Цель кратчайшего пути не может быть найдена')
        print(-1)
    # Конец определения условий
    if src == dest:
        # Строим кратчайший путь и отображаем его
        path = []
        pred = dest
        while pred != None:
            path.append(pred)
            pred = predecessors.get(pred, None)
        # Изменяет массив на противоположный, чтобы восстановить путь
        readable = path[0]
        for index in range(1, len(path)):
            readable = str(path[index]) + ' ' + str(readable)
        # Распечываем результат
        # print('shortest path - array: ' + str(path))
        # print("path: " + readable + ",   cost=" + str(distances[dest]))
        # the_way = list(map(int, readable.split()))
        print(readable)
        # print(distances[dest])
    else:
        # Если это начальный запуск, инициализирует стоимость
        if not visited:
            distances[src] = 0
        # Посещение соседних вершин
        for neighbor in graph[src]:
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        # Отмечаем посещенные вершины
        visited.append(src)
        # теперь, когда все соседи посещены: рекурсия
        # выбрать не посещённый узел с наименьшим расстоянием 'x'
        # Запустить алгоритм Декстра с точкой назначения ='x'
        unvisited = {}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k, float('inf'))
        x = min(unvisited, key=unvisited.get)
        dijkstra(graph, x, dest, visited, distances, predecessors)


def read_and_run():
    """ Считывает матричный граф и параметры задачи, перводит в словарь словарей и
    запускает алгоритм Декстры"""
    # N - количество вершин графа (количество городов - последующих строк в матрице смежности)
    # S - начальная вершина графа (пункт отправления)
    # F - конечная вершина графа (пункт назначения)
    # G - список списков - представление графа в матричном виде
    # distances  - словарь словарей - представление графа в корректном виде для запуска алгоритма
    N, S, F = map(int, input().split())
    G = []
    distances = {}
    # считываем условия задачи в словари
    for i in range(N):
        G.append(list(map(int, input().split())))
    # приводим граф к нужной структуре данных - списку списков
    for i in range(len(G)):
        temp = {}
        for j in range(len(G)):
            if j != i:
                temp[j + 1] = G[i][j]
        distances[i + 1] = temp

    dijkstra(distances, S, F)

read_and_run()