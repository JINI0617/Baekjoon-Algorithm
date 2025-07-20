num = int(input())
words = []
for i in range(num):
    word = input()
    words.append(word)

book_count = {}
for word in words:
    if word in book_count:
        book_count[word] += 1
    else:
        book_count[word] = 1

max_count = max(book_count.values())

most_common = [word for word in book_count if book_count[word] == max_count]
print(min(most_common))