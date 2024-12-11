from collections import Counter

L = Counter(map(int, open("11.input").read().strip().split()))
for it in range(75):
    N = Counter()
    while L:
        n, m = L.popitem()
        if n == 0:
            N[1] += m
        elif len(a := str(n)) % 2 == 0:
            N[int(a[: len(a) // 2])] += m
            N[int(a[len(a) // 2 :])] += m
        else:
            N[n * 2024] += m
    if it == 24:
        print(f"Part 1: {sum(N.values())}")
    if it == 74:
        print(f"Part 2: {sum(N.values())}")
        break
    L = N
