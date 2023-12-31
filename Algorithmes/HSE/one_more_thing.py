def main():
    input_file = open("input.txt", "r")
    output_file = open("output.txt", "w")
    inf = 10 ** 9
    a = []
    b = []
    c = []
    d = []
    line = input_file.readline().split()
    n = int(line[0])
    line = input_file.readline().split()
    s, f = int(line[0]), int(line[1])
    line = input_file.readline().split()
    m = int(line[0])

    for i in range(m):
        line = input_file.readline().split()
        a.append(int(line[0]))
        b.append(int(line[1]))
        c.append(int(line[2]))
        d.append(int(line[3]))

    print(a)
    print(b)
    print(c)
    print(d)

    distination = []
    for i in range(n):
        distination.append(inf)

    distination[s - 1] = 0
    for i in range(n - 1):
        for j in range(m):
            if distination[c[j] - 1] > d[j] and distination[a[j] - 1] != inf and b[j] >= distination[a[j] - 1]:
                distination[c[j] - 1] = d[j]

    for i in range(n):
        if distination[i] == inf:
            distination[i] = 0

    print(distination)

    for i in range(n):
        if distination[i] == 0:
            distination[i] = -1
            distination[s - 1] = 0

    ans = distination[f - 1]
    print(ans)

    output_file.write(str(ans) + "\n")
    input_file.close()
    output_file.close()


if __name__ == "__main__":
    main()