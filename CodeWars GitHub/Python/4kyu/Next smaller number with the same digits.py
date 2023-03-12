def next_smaller(n):
    s = list(str(n))
    i = j = len(s) - 1
    while i > 0 and s[i - 1] <= s[i]: i -= 1
    if i <= 0: return -1
    while s[j] >= s[i - 1]: j -= 1
    s[i - 1], s[j] = s[j], s[i - 1]
    s[i:] = reversed(s[i:])
    if s[0] == '0': return -1
    return int(''.join(s))


# ----------------------------------------------

def next_smaller2(n):
    s = list(str(n))
    for i in range(len(s) - 2, -1, -1):

        if s[i] > s[i + 1]:
            t = s[i:]
            m = max(filter(lambda x: x < t[0], t))
            t.remove(m)
            t.sort(reverse=True)
            s[i:] = [m] + t
            if int(s[0]) != 0:
                return int("".join(s))

    return -1