from collections import Counter

L = list(tuple(map(lambda x: int(x), item.split())) for item in open("01.input").readlines())

# part 1:
lside = sorted(item[0] for item in L)
rside = sorted(item[1] for item in L)

p1 = sum(abs(lside[ind] - rside[ind]) for ind in range(len(lside)))
print(p1)

# part 2:
C = Counter(rside)
p2 = sum(ind * C[ind] for ind in lside)
print(p2)
