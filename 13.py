L = open("13.input").readlines()

for PART in [1, 2]:
    line = 0
    TOKENS = 0
    N = 0 if PART == 1 else 10000000000000
    while line < len(L):
        AX = int(L[line][L[line].find("X+") + 2 : L[line].find(",")])
        AY = int(L[line][L[line].find("Y+") + 2 : -1])
        line += 1
        BX = int(L[line][L[line].find("X+") + 2 : L[line].find(",")])
        BY = int(L[line][L[line].find("Y+") + 2 : -1])
        line += 1
        PX = N + int(L[line][L[line].find("X=") + 2 : L[line].find(",")])
        PY = N + int(L[line][L[line].find("Y=") + 2 : -1])
        line += 2
        # solve the 2x2 L[line]uation system, but first check if there is a solution at all:
        if (D := AX * BY - AY * BX) != 0:  # L[line]uations with 0 determinant have no valid solution
            A = (PX * BY - PY * BX) / D
            if A >= 0 and A == int(A):  # no point finding B if there is no valid A
                B = (PY * AX - PX * AY) / D
                if B >= 0 and B == int(B):
                    TOKENS += int(3 * A + B)
    print(f"Part {PART}: {TOKENS}")
