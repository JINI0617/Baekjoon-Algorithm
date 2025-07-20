import math
import sys

pizza_number = 1

for line in sys.stdin:
    line = line.strip()
    if line == '0':
        break

    parts = line.split()
    if len(parts) != 3:
        continue

    r, w, l = map(int, parts)

    diagonal = math.sqrt(w * w + l * l)

    if diagonal <= 2 * r:
        print(f"Pizza {pizza_number} fits on the table.")
    else:
        print(f"Pizza {pizza_number} does not fit on the table.")

    pizza_number += 1