from collections import deque

L = deque(open("03.input").read())
# L = deque("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
D = set("0123456789")
p2 = 0
do = True
while L:
    if (f := L.popleft()) == "m":
        if L.popleft() == "u":
            if L.popleft() == "l":
                if L.popleft() == "(":
                    a = ""
                    b = ""
                    keepgoing = True
                    while True:
                        c = L.popleft()
                        if c in D:
                            a += c
                        elif c == ",":
                            break
                        else:
                            keepgoing = False
                            break
                    if not keepgoing:
                        continue
                    else:
                        keepgoing = True
                        while True:
                            c = L.popleft()
                            if c in D:
                                b += c
                            elif c == ")":
                                break
                            else:
                                keepgoing = False
                                break
                    if not keepgoing:
                        continue
                    if do:
                        p2 += int(a) * int(b)
    elif f == "d":
        if L.popleft() == "o":
            if (g := L.popleft()) == "n":
                if L.popleft() == "'":
                    if L.popleft() == "t":
                        if L.popleft() == "(":
                            if L.popleft() == ")":
                                do = False
            elif g == "(":
                if L.popleft() == ")":
                    do = True
print(f"Part 2: {p2}")
