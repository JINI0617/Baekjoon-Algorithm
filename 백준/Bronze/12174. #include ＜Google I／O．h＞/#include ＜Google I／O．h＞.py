val = {'O': '0', 'I':'1'}

n = int(input())

for i in range(1, n+1):
    B = int(input())
    a = input().replace(" ", "") #공백제거

    s = ''.join(val[ch] for ch in a)
    result = ""

    for j in range(B):
        byte = s[j*8:(j+1)*8]
        result += chr(int(byte, 2))

    print(f"Case #{i}: {result}")

    

    