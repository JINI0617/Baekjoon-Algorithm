def is_group_word(word):
    seen = [False] * 26
    prev = ''
    
    for c in word:
        if c != prev:
            if seen[ord(c) - ord('a')]:
                return False
            seen[ord(c) - ord('a')] = True
        prev = c
    
    return True


N = int(input())
count = 0

for _ in range(N):
    word = input()
    if is_group_word(word):
        count += 1

print(count)
