n = int(input())

def IsPrime(n):
    if n < 2:
        return 'NO'
    if n < 4:
        return 'YES'
    if n % 2 == 0:
        return 'NO'
    for i in range(3, n, 2):
        if i * i > n:
            break
        if n % i == 0:
            return 'NO'
    return 'YES'


print(IsPrime(n))
