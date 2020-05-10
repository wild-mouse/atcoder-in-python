import fileinput

n = int(input())

c = 0
for i in range(1, n + 1):
    cc = 0
    if i % 2 == 0:
        continue
    for j in range(1, i + 1):
        if i % j == 0:
            cc += 1
    if cc == 8:
        c += 1

print(c)
