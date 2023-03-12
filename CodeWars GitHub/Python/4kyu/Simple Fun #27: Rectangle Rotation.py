def rectangle_rotation(a, b):
    a //= 2**0.5
    b //= 2**0.5
    r = (a + 1) * (b + 1) + a * b
    return r + r % 2 - 1
