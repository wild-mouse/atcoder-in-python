import fileinput

s = list(input())

if s[0] != "A" or s[1].isupper() or s[len(s) - 1].isupper():
    print("WA")
    exit()

cc = False
for i in range(2, len(s) - 1):
    if s[i] == "C" and not cc:
        cc = True
        continue
    if s[i] == "C" and cc:
        print("WA")
        exit()
    if s[i].isupper() and s[i] != "C":
        print("WA")
        exit()

if cc:
    print("AC")
else:
    print("WA")



