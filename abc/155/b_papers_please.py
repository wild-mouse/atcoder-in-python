import fileinput

n = int(input())

a = list(map(int, input().split()))

b = True

for i in range(n):
    aa = a[i]
    if aa % 2 != 0:
        continue
    if aa % 3 != 0 and aa % 5 != 0:
        b = False
        break

if b:
    print("APPROVED")
else:
    print("DENIED")

