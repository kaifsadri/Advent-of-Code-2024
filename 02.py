L = list(tuple(map(lambda x: int(x), item.split())) for item in open("02.input").readlines())


def is_safe(line):
    m = line[1] - line[0]
    if not (1 <= abs(m) <= 3):
        return False
    for ind in range(2, len(line)):
        nm = line[ind] - line[ind - 1]
        if nm * m < 0:
            return False
        if not 1 <= abs(nm) <= 3:
            return False
        m = nm
    return True


# Part 1:
Safe = set()
for ind in range(len(L)):
    if is_safe(L[ind]):
        Safe.add(ind)
print(len(Safe))

# part 2:
for ind in range(len(L)):
    if ind in Safe:
        continue
    l = L[ind]
    for c in range(len(l)):
        if c == 0:
            if is_safe(l[1:]):
                Safe.add(ind)
                break
        elif c == len(l):
            if is_safe(l[:-1]):
                Safe.add(ind)
                break
        else:
            if is_safe(l[:c] + l[c + 1 :]):
                Safe.add(ind)
                break
print(len(Safe))
