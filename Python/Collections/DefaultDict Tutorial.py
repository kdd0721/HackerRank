from collections import defaultdict
d = defaultdict(list)
n, m = map(int, input().split())

for i in range(n):
    d[input()].append(i+1)

for i in range(m):
    ch = input()
    if ch in d.keys():
        print(*d[ch])
    else:
        print(-1)