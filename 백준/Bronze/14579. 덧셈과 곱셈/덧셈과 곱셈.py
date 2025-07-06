a, b = map(int, input().split())
result = 1
for i in range(a, b+1):
    result *= i*(i+1)//2

print(result % 14579)