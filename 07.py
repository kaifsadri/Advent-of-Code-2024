E = dict()
for line in open("07.input").readlines():
    E[int(line[: line.find(":")])] = list(map(int, line[line.find(":") + 1 :].split()))


def poss1(target, eq: list) -> bool:
    n = eq[-1]
    if len(eq) == 1:
        return target == eq[0]
    if target % n == 0:
        if poss1(target // n, eq[:-1]):
            return True
    if target >= n:
        if poss1(target - n, eq[:-1]):
            return True
    return False


p1 = 0
for t in E:
    if poss1(t, E[t]):
        p1 += t
print(f"Part 1: {p1}")


def poss2(target, eq: list) -> bool:
    n = eq[-1]
    if len(eq) == 1:
        return target == eq[0]
    if target % n == 0:
        if poss2(target // n, eq[:-1]):
            return True
    if target >= n:
        if poss2(target - n, eq[:-1]):
            return True
        digs = len(str(n))
        if str(target)[-digs:] == str(n) and len(str(target)) > len(str(n)):
            if poss2(int(str(target)[:-digs]), eq[:-1]):
                return True
    return False


p2 = 0
for t in E:
    if poss2(t, E[t]):
        p2 += t
print(f"Part 2: {p2}")
