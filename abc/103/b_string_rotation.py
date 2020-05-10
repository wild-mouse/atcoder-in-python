import fileinput

s = input()
t = input()

if s == t:
    print("Yes")
    exit()

for i in range(1, len(s)):
    if t == s[i:] + s[:i]:
        print("Yes")
        exit()

print("No")


