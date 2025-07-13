import sys

input = sys.stdin.readline

n, m = map(int, input().split())

a = set()
for _ in range(n):
    a.add(input().strip())

res = []
for _ in range(m):
    name = input().strip()
    if name in a:
        res.append(name)

res.sort()

print(len(res))
for name in res:
    print(name)
