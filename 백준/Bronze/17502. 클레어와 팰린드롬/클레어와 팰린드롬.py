n = int(input())
s = list(input())  

for i in range(n // 2):
    left = s[i]
    right = s[n - 1 - i]

    if left == '?' and right == '?':
        s[i] = s[n - 1 - i] = 'a'
    elif left == '?':
        s[i] = right 
    elif right == '?':
        s[n - 1 - i] = left
    elif left != right:
        print("Not a palindrome") 
        break

if n % 2 == 1 and s[n // 2] == '?':
    s[n // 2] = 'a'

print(''.join(s))
