R = list()
for line in open("14.input").readlines():
    p, v = line.split()
    R.append([list(map(int, p[2:].split(","))), list(map(int, v[2:].split(",")))])
X, Y = 101, 103
for sec in range(100):
    for r in R:
        r[0][0] = (r[0][0] + r[1][0]) % X
        r[0][1] = (r[0][1] + r[1][1]) % Y
Q1 = Q2 = Q3 = Q4 = 0
for r in R:
    x, y = r[0]
    if x < X // 2 and y < Y // 2:
        Q1 += 1
    elif X // 2 < x and y < Y // 2:
        Q2 += 1
    elif x < X // 2 and Y // 2 < y:
        Q3 += 1
    elif X // 2 < x and Y // 2 < y:
        Q4 += 1
print(f"Part 1: {Q1 * Q2 * Q3 * Q4}")
