B = set(
    complex(int(line.split(",")[1]), int(line.split(",")[0]))
    for line in open("18.input").readlines()[:1024]
)
been = {0: 0}
while True:
    new = dict(
        (p + d, been[p] + 1)
        for d in {1, -1, 1j, -1j}
        for p in been
        if (p + d) not in B
        and 0 <= (p + d).real <= 70
        and 0 <= (p + d).imag <= 70
        and ((p + d) not in been or been[(p + d)] > been[p] + 1)
    )
    if new:
        been.update(new)
    else:
        break
print(f"Part 1: {been[70 + 70j]}")
