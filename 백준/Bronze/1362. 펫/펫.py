scenario = 1

while True:
    o_w = input().split()
    o, w = map(int, o_w)
    if o == 0 and w == 0:
        break

    dead = False

    while True:
        action, n = input().split()
        n = int(n)
        if action == "#" and n == 0:
            break
        if dead:
            continue
        if action == "E":
            w -= n
        elif action == "F":
            w += n
        if w <= 0:
            dead = True

    print(scenario, end=' ')
    if dead:
        print("RIP")
    elif o / 2 < w < o * 2:
        print(":-)")
    else:
        print(":-(")
    scenario += 1
