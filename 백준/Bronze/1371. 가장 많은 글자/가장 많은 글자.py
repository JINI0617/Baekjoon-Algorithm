import sys
from collections import Counter

s = sys.stdin.read().replace('\n', '')
cnt = Counter(filter(str.isalpha, s))

m = max(cnt.values())
res = [c for c in cnt if cnt[c] == m]

print(''.join(sorted(res)))
