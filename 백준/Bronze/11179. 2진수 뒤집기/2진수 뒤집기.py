N = int(input())

binary = bin(N)[2:]
reversed_binary = binary[::-1]

result = int(reversed_binary, 2)
print(result)
