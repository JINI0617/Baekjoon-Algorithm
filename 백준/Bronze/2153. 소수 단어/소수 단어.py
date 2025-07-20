def is_prime(n):
    if n == 1:
        return True 
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

word = input()
sum = 0

for c in word:
    if c.isupper():
        sum += ord(c) - ord('A') + 27
    elif c.islower():
        sum += ord(c) - ord('a') + 1

if is_prime(sum):
    print("It is a prime word.")
else:
    print("It is not a prime word.")
