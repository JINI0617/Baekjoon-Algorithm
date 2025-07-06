A, B = map(int, input().split())
N = int(input())

favorites = []
for _ in range(N):
    favorites.append(int(input()))

min_count = abs(A - B)

for fav in favorites:
    count = abs(fav - B) + 1
    if count < min_count:
        min_count = count

print(min_count)

# 다시 풀어보기!!