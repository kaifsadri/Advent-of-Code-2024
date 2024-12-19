from functools import cache

P = list(line.strip() for line in open("19.input").readlines())


@cache
def poss(pattern):
    global P
    result = 0
    if pattern == "":
        return 1
    for t in P[0].split(", "):
        if pattern.startswith(t):
            result += poss(pattern[len(t) :])
    return result


P1 = P2 = 0
for p in P[2:]:
    if a := poss(p):
        P1 += 1
        P2 += a
print(f"Part 1: {P1}")
print(f"Part 2: {P2}")
