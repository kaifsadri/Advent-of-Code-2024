Moves = list()
Boxes = set()
Robot = tuple()
Walls = set()
D = {">": 1j, "^": -1, "<": -1j, "v": 1}
for row, line in enumerate(open("/home/tv/Desktop/AoC 2024/15/15.input").readlines()):
    for col, c in enumerate(line):
        match c:
            case "O":
                Boxes.add(complex(row, col))
            case "#":
                Walls.add(complex(row, col))
            case "@":
                Robot = complex(row, col)
            case ">" | "^" | "<" | "v":
                Moves.append(c)


def move(p, d):
    global Walls, Robot, Boxes
    np = p + D[d]
    if np in Walls:
        return False
    elif np in Boxes:
        if move(np, d):
            return move(p, d)
    else:  # np is empty space
        if Robot == p:
            Robot = np
            return True
        else:
            Boxes.add(np)
            Boxes.remove(p)
            return True


for m in Moves:
    move(Robot, m)
print(f"Part 1: {int(sum(100 * box.real + box.imag for box in Boxes))}")
