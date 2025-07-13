T = int(input())

for _ in range(T):
    s = input()
    score = 0
    combo = 0

    for ch in s:
        if ch == 'O':
            combo += 1
            score += combo
        else:
            combo = 0

    print(score)
