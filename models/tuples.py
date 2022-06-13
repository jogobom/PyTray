def tuple(x, y, z, w):
    return {'x': float(x), 'y': float(y), 'z': float(z), 'w': float(w)}


def point(x, y, z):
    return tuple(x, y, z, 1.0)


def vector(x, y, z):
    return tuple(x, y, z, 0.0)


def equals(a, b):
    def eqval(m, n):
        EPSILON = 1e-6
        return abs(m - n) < EPSILON

    return eqval(a['x'], b['x']) and eqval(a['y'], b['y']) and eqval(a['z'], b['z']) and eqval(a['w'], b['w'])
