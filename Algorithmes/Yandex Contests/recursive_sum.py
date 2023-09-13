def summ(a):
    if a == 0:
        return 0
    return a + summ(a-1)

y = summ(5)

print(y)
