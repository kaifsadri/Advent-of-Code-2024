G = dict()
for R, ro in enumerate(open("08.input").readlines()):
    for C, item in enumerate(ro.strip()):
        if item != ".":
            G[(R, C)] = item

# Part 1:
A = set()
for a1 in G:
    for a2 in G:
        if a1 != a2 and G[a1] == G[a2]:
            dr = a1[0] - a2[0]
            dc = a1[1] - a2[1]
            A.add((a1[0] + dr, a1[1] + dc))
            A.add((a2[0] - dr, a2[1] - dc))
print(f"Part 1: {sum(1 for item in A if 0<=item[0]<=R and 0<=item[1]<=C)}")

# Part 2:
A.clear()  # this is not necessary. just here for clean code
for a1 in G:
    for a2 in G:
        if a1 != a2 and G[a1] == G[a2]:
            dr = a1[0] - a2[0]
            dc = a1[1] - a2[1]
            for n in range(max(C, R)):  # prolly faster than checking every single antinode
                A.add((a1[0] + n * dr, a1[1] + n * dc))
                A.add((a2[0] - n * dr, a2[1] - n * dc))
print(f"Part 2: {sum(1 for item in A if 0<=item[0]<=R and 0<=item[1]<=C)}")
