# puzzle input:
A = 30553366
B = 0
C = 0
Program = [2, 4, 1, 1, 7, 5, 4, 7, 1, 4, 0, 3, 5, 5, 3, 0]


def combo(x):
    global A, B, C
    match x:
        case 0 | 1 | 2 | 3:
            return x
        case 4:
            return A
        case 5:
            return B
        case 6:
            return C


insptr = 0
output = list()
try:
    while True:
        ins, opr = Program[insptr], Program[insptr + 1]
        # print(insptr, ins, opr)
        match ins:
            case 0:
                A = int(A / (2 ** combo(opr)))
                insptr += 2
            case 1:
                B = B ^ opr
                insptr += 2
            case 2:
                B = combo(opr) % 8
                insptr += 2
            case 3:
                if A != 0:
                    insptr = opr
                else:
                    insptr += 2
            case 4:
                B = B ^ C
                insptr += 2
            case 5:
                output.append(str(combo(opr) % 8))
                insptr += 2
            case 6:
                B = int(A / (2 ** combo(opr)))
                insptr += 2
            case 7:
                C = int(A / (2 ** combo(opr)))
                insptr += 2
except IndexError:
    print(f"Part 1: {",".join(output)}")
