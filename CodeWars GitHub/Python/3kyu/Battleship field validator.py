from scipy.ndimage.measurements import label, find_objects, np
def validate_battlefield(field):
    field = np.array(field)
    return sorted(
        ship.size if min(ship.shape) == 1 else 0
        for ship in (field[pos] for pos in find_objects(label(field, np.ones((3,3)))[0]))
    ) == [1,1,1,1,2,2,2,3,3,4]


# -----------------------------------------

def validateBattlefield2(field):
    n, m = len(field), len(field[0])
    def cell(i, j):
        if i < 0 or j < 0 or i >= n or j >= m: return 0
        return field[i][j]
    def find(i, j):
        if cell(i + 1, j - 1) or cell(i + 1, j + 1): return 10086
        if cell(i, j + 1) and cell(i + 1, j): return 10086
        field[i][j] = 2
        if cell(i, j + 1): return find(i, j + 1) + 1
        if cell(i + 1, j): return find(i + 1, j) + 1
        return 1
    num = [0] * 5
    for i in xrange(n):
        for j in xrange(m):
            if cell(i, j) == 1:
                r = find(i, j)
                if r > 4: return False
                num[r] += 1
    [tmp, submarines, destroyers, cruisers, battleship] = num
    return battleship == 1 and cruisers == 2 and destroyers == 3 and submarines == 4
