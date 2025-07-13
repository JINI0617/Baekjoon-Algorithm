n = input()

cnt = [0] * 10

for ch in n:
    cnt[int(ch)] += 1

cnt[6] = (cnt[6] + cnt[9] + 1) // 2

print(max(cnt[:9]))

