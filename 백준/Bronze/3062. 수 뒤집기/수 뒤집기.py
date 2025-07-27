t = int(input())

for i in range(t):
    n = int(input())
    reverse_n = int(str(n)[::-1])
    num = n + reverse_n
    
    if(str(num) == str(num)[::-1]):
        print("YES")
    else:
        print("NO")