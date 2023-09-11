a = int(input())
n = int(input())


def power(a, n):
    if n == 0:
        return 1
    return power(a, n - 1) * a


result = power(a, n)

print(result)
