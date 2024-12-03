from collections import deque

L = deque(open("03.input").read())
# L = deque("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")
D = set("0123456789")
p1 = 0
while L:
    if L.popleft() == "m":
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
                    print(f"mul({a},{b})")
                    p1 += int(a) * int(b)
print(f"Part 1: {p1}")
