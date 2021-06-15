import time

start = time.perf_counter()
puzzle = list()
with open('day17.txt', 'r') as f:
    puzzle = f.readlines()
    f.close()

active_cubes = set()
inactive_cubes = set()
neighbors_dict = dict()
mode = ''

def find_neighbors(key):
    if mode == '3D':
        x, y, z = key
    else:
        x, y, z, w = key
    n = set()
    if key in neighbors_dict.keys():
        return neighbors_dict.get(key)
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                if mode == '3D':
                    n_key = (i, j, k)
                    n.add(n_key)
                else:
                    for l in range(w - 1, w + 2):
                        n_key = (i, j, k, l)
                        n.add(n_key)
    if mode == '3D':
        n.remove((x, y, z))
    else:
        n.remove((x, y, z, w))
    neighbors_dict[key] = n
    return n

def find_inactive_neighbors(key):
    i_n = set()
    for n in find_neighbors(key):
        if n not in active_cubes:
            if n not in i_n:
                i_n.add(n)
    return i_n

def count_active_neighbors(key):
    c = 0
    for n in find_neighbors(key):
        if n in active_cubes:
            c += 1
    return c

# initialize the set of active cubes
def get_initial_cubes(mode):
    cubes = set()
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y].strip())):
            if (puzzle[y][x]) == '#':
                if mode == '3D':
                    key = (x, y, 0)
                else:
                    key = (x, y, 0, 0)
                cubes.add(key)
    return cubes

def find_inactive_cubes():
    inactive_cubes = set()
    for a_c in active_cubes:
        inactive_cubes = inactive_cubes.union(find_inactive_neighbors(a_c))
    return inactive_cubes

def apply_rules():
    new_actives = set()
    for cube in active_cubes:
        if count_active_neighbors(cube) in [2, 3]:
            new_actives.add(cube)
    for cube in inactive_cubes:
        if count_active_neighbors(cube) == 3:
            new_actives.add(cube)
    return new_actives


def run(m):
    global active_cubes, inactive_cubes, mode
    mode = m
    active_cubes = get_initial_cubes(mode)
    for i in range(6):
        inactive_cubes = find_inactive_cubes()
        active_cubes = apply_rules()
    print(len(active_cubes))

run('3D')
run('4D')
end = time.perf_counter()
print("Completed in {}ms.".format(end - start) * 10000)