def convert(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
    res = ""
    while n > 0:
        res = digits[n % base] + res
        n //= base
    return res

T = int(input())
for _ in range(T):
    N = int(input())
    found = False
    for B in range(2, 65):
        rep = convert(N, B)
        if rep == rep[::-1]:  # 회문인지 확인
            found = True
            break
    print(1 if found else 0)
