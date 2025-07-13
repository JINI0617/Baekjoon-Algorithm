input_line = input().strip()  # 앞뒤 공백 제거

count = 0

if input_line != "":
    for i in range(len(input_line)):
        if input_line[i] != ' ' and (i == 0 or input_line[i - 1] == ' '):
            count += 1

print(count)
#다시풀기