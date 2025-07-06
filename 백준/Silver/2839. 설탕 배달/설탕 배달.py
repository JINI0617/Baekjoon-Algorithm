N = int(input())

for five_count in range(N // 5, -1, -1):
    remain = N - (five_count * 5)

    if remain % 3 == 0:
        print(five_count + (remain // 3))
        break
else:
    print(-1)
