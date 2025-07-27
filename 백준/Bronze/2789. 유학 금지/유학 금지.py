str = list(input())
cam = list('CAMBRIDGE')
result = []

for st in str:
    if st not in cam:
        result.append(st)

print(''.join(result))