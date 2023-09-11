a = int(input())
n = int(input())


def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return power(a, n - 1) * a
    else:
        return power(a, n // 2) ** 2

result = power(a, n)

print(result)
