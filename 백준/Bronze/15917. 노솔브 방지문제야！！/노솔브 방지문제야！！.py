import sys
input = sys.stdin.readline

Q = int(input())

for i in range (Q):
    a = int(input())

    while a % 2 == 0:
        a //= 2
    
    if a == 1:
        print(1)
    else:
        print(0)