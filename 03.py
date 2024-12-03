from re import findall
from math import prod

L = open("03.input").read()

# part 1
pat = r"mul\(\d+,\d+\)"
matches = findall(pat, L)
print(f"Part 1: {sum(prod(map(int, m[4:-1].split(","))) for m in matches)}")

# part 2
pat = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"
matches = findall(pat, L)
p2 = 0
do = True
for m in matches:
    match m:
        case "do()":
            do = True
        case "don't()":
            do = False
        case _:
            if do:
                p2 += prod(map(int, m[4:-1].split(",")))
print(f"Part 2: {p2}")
