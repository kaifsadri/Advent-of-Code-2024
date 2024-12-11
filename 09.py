from collections import deque

# Part 1: just follow instructions
P = deque(map(int, open("09.input").read().strip()))
if len(P) % 2:
    P.append(0)
L = P.copy()
disk = deque()
blockid = -1
while L:
    blockid += 1
    for i in range(L.popleft()):
        disk.append(blockid)
    for i in range(L.popleft()):
        disk.append(-1)
CD = deque()
try:
    while True:
        t = disk.popleft()
        if t != -1:
            CD.append(t)
        else:
            while True:
                n = disk.pop()
                if n != -1:
                    CD.append(n)
                    break
except IndexError:
    pass
print(f"Part 1: {sum(i * CD[i] for i in range(len(CD)))}")

# Part 2 models the disk like a linked list of files, ignoring free space
L = P.copy()
disk = dict()
file_id = -1
start = 0
while L:
    file_id += 1
    block_len = L.popleft()
    # now build the file:
    disk[file_id] = [
        start,
        start + block_len - 1,
        file_id - 1,
        file_id + 1,
    ]  # at start, all files are in order
    start += block_len + L.popleft()
max_file_id = file_id

# to compress the disk, we start from last file, find a hole and stick it in there.
for file_id in range(max_file_id, 0, -1):
    start, end, prev_file_id, next_file_id = disk[file_id]
    block_len = end - start + 1
    fid = 0
    while True:
        if fid == file_id:  # this means we are getting past the original location
            break
        st, en, pr, nx = disk[fid]
        f1 = en + 1
        f2 = disk[nx][0] - 1
        if f2 - f1 + 1 >= block_len:  # this is a space we can fit our file in
            # move the current file_id here
            disk[file_id] = [f1, f1 + block_len - 1, fid, nx]
            disk[fid][3] = file_id
            disk[nx][2] = file_id
            disk[prev_file_id][3] = next_file_id
            if next_file_id < max_file_id:
                disk[next_file_id][2] = prev_file_id
            break
        fid = nx
print(f"Part 2: {sum(sum(fid*loc for loc in range(disk[fid][0], disk[fid][1]+1)) for fid in disk)}")
