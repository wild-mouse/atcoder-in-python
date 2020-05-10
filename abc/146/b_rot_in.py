import fileinput

n = int(input())


def slip(c):
    return chr(((ord(c) - 65 + n) % 26) + 65)


s = list(input())

for i in range(len(s)):
    s[i] = slip(s[i])

print("".join(s))
