import fileinput

n = int(input())

a = False

for i in range(1, 10):
    for j in range (1, 10):
        if i * j == n:
            a = True

if a:
    print("Yes")
else:
    print("No")