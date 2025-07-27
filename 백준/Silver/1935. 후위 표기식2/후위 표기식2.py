n = int(input())
expr = input()

values = []
for _ in range(n):
    values.append(float(input()))

stack = []

for ch in expr:
    if 'A' <= ch <= 'Z':
        stack.append(values[ord(ch) - ord('A')])
    else:
        b = stack.pop()
        a = stack.pop()
        if ch == '+':
            stack.append(a + b)
        elif ch == '-':
            stack.append(a - b)
        elif ch == '*':
            stack.append(a * b)
        elif ch == '/':
            stack.append(a / b)

print(f"{stack[-1]:.2f}")
