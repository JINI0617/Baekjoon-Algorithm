import sys

N = int(sys.stdin.readline())

nums = []
for _ in range(N):
    num = int(sys.stdin.readline())
    nums.append(num)

nums.sort(reverse=True)

for num in nums:
    print(num)
