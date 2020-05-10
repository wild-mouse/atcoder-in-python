import fileinput

n = int(input())
nn = list(map(int, str(n)))

if n % sum(nn) == 0:
    print("Yes")
else:
    print("No")
