R = list()
for line in open("14.input").readlines():
    p, v = line.split()
    R.append([list(map(int, p[2:].split(","))), list(map(int, v[2:].split(",")))])
X, Y = 101, 103
for sec in range(1, 100000):
    # Printing cases where no two robots overlap reduces the cases we need to checkc by hand
    S = set()
    for r in R:
        r[0][0] = (r[0][0] + r[1][0]) % X
        r[0][1] = (r[0][1] + r[1][1]) % Y
        S.add((r[0][0], r[0][1]))
    if len(S) == len(R):
        print("\n" * Y)
        for y in range(Y):
            for x in range(X):
                if (x, y) in S:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        input(f"Part 2 candidate after {sec}s. CTRL+C to stop. ENTER to continue.")
