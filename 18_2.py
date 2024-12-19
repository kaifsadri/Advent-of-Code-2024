P = list(
    complex(int(line.split(",")[1]), int(line.split(",")[0]))
    for line in open("18.input").readlines()
)
upper = len(P) - 1
lower = 1024
while True:
    if upper == lower + 1:
        print(f"Part 2: {int(P[lower].real)},{int(P[lower].imag)}")
        break
    been = {0}
    B = set(P[: (upper + lower) // 2])
    while True:
        new = set(
            p + d
            for d in {1, -1, 1j, -1j}
            for p in been
            if (p + d) not in B
            and (p + d) not in been
            and 0 <= (p + d).real <= 70
            and 0 <= (p + d).imag <= 70
        )
        if 70 + 70j in new:  # search higher
            lower = (upper + lower) // 2
            break
        elif not new:  # search lower
            upper = (upper + lower) // 2
            break
        else:
            been |= new
