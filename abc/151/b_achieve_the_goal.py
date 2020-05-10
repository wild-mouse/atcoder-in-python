import fileinput

n, k, m = map(int, input().split())

a = list(map(int, input().split()))

g = n * m

gg = g - sum(a)

if gg > k:
    print(-1)
else:
    print(max(0, gg))
