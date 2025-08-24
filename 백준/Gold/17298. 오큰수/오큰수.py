import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

ans = [-1] * n    
st = []                

for i in range(n):

    while st and A[st[-1]] < A[i]:
        ans[st.pop()] = A[i]
    st.append(i)

print(*ans)
