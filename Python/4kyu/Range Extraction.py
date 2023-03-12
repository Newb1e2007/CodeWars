def solution(args):
    out = []
    beg = end = args[0]

    for n in args[1:] + [""]:
        if n != end + 1:
            if end == beg:
                out.append(str(beg))
            elif end == beg + 1:
                out.extend([str(beg), str(end)])
            else:
                out.append(str(beg) + "-" + str(end))
            beg = n
        end = n

    return ",".join(out)


# ----------------------------------------------------

def solution2(arr):
    ranges = []
    a = b = arr[0]
    for n in arr[1:] + [None]:
        if n != b + 1:
            ranges.append(str(a) if a == b else "{}{}{}".format(a, "," if a + 1 == b else "-", b))
            a = n
        b = n
    return ",".join(ranges)


# ----------------------------------------------------

from itertools import groupby
def solution3(args):
    grps = ([v[1] for v in g] for _, g in groupby(enumerate(args), lambda p: p[1] - p[0]))
    return ','.join('{}{}{}'.format(g[0], '-' if len(g) > 2 else ',', g[-1])
                    if len(g) > 1 else str(g[0]) for g in grps)
