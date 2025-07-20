line = input()
arr = list(map(int, line.split()))

is_good = True
for i in range(1, len(arr)):
    if arr[i - 1] > arr[i]:
        is_good = False
        break

if is_good:
    print("Good")
else:
    print("Bad")
