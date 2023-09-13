n = int(input())
k = int(input())


def c(n, k):
    if n == k or k == 0:
        return 1
    if k != 1:
        return c(n - 1, k - 1) + c(n - 1, k)
    else:
        return n


result = c(n, k)

print(result)
