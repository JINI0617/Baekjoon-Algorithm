k = int(input())

for i in range(k):
    a, b, c, d, e = map(int, input().split())
    sum = a * 350.34 + b * 230.90 + c * 190.55 + d * 125.30 + e * 180.90
    print(f"${sum:.2f}")