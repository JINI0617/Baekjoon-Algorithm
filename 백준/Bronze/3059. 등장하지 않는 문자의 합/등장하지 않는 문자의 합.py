T = int(input())

for _ in range(T):
    S = input().strip()
    appeared = set(S)  

    total = 0
    for ch in map(chr, range(65, 91)):  
        if ch not in appeared:
            total += ord(ch)

    print(total)
