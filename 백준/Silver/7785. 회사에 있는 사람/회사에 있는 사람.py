num = int(input())
status = set()

for _ in range(num):
    name, state = input().split()
    if state == 'enter':
        status.add(name)
    else:
        status.discard(name)  # 안전하게 삭제

for name in sorted(status, reverse=True):
    print(name)
