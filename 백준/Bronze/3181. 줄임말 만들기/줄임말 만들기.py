a = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili' ]

words = input().split()

for word in words:
    if word not in a:
        print(word[0].upper(), end='')
    else:
        if word == words[0]:
            print(word[0].upper(), end='')
        else:
            continue

