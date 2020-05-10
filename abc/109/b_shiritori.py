import fileinput

n = int(input())

ws = list()
ws.append(input())
for i in range(n - 1):
    w = input()
    if w in ws or ws[-1][-1] != w[0]:
        print("No")
        exit()
    ws.append(w)

print("Yes")
