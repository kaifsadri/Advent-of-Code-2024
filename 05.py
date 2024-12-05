from collections import defaultdict

L = open("05.input").readlines()
C = set()
E = set()
Correct = set()
k = 0
while True:
    C.add(tuple(map(int, L[k].strip().split("|"))))
    k += 1
    if L[k].strip() == "":
        k += 1
        break

try:
    while True:
        E.add(tuple(map(int, L[k].strip().split(","))))
        k += 1
except IndexError:
    pass

# Part 1:
p1 = 0
for update in E:
    flag = True
    for m in range(len(update) - 1):
        for n in range(m + 1, len(update)):
            if (update[n], update[m]) in C:
                flag = False
    if flag:
        Correct.add(update)  # used in part 2
        p1 += update[len(update) // 2]
print(f"Part 1: {p1}")

# Part 2:
# Since every update is possible to correct, the middle page is the one that falls before half of the others
p2 = 0
for update in E:
    if update in Correct:
        continue
    cnt = defaultdict(lambda: 0)
    for m in range(len(update)):
        for n in range(len(update)):
            if (update[m], update[n]) in C:
                cnt[update[m]] += 1
    for item in cnt:
        if cnt[item] == len(update) // 2:
            p2 += item
print(f"Part 2: {p2}")
