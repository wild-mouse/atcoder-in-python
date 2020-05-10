import fileinput

n = int(input())

if n % 2 != 0:
    print("No")
    exit(0)

s = input()

if s[0:int(len(s) / 2)] == s[int(len(s) / 2):]:
    print("Yes")
else:
    print("No")