import statistics


s = int(input())
l = list(map(int, input().split()))
res = int(statistics.median(l))
print(res)