import fileinput

n = int(input())
s, t = input().split()

ss = ""
for i in range(n):
    ss += s[i] + t[i]

print(ss)
