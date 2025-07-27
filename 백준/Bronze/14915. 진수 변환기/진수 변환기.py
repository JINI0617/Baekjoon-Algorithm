m, n = map(int, input().split())
digits = "0123456789ABCDEF"
result = ""

if m == 0:
    result = "0"
else:
    while m > 0:
        result = digits[m % n] + result
        m //= n

print(result)