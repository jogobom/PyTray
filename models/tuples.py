class Tuple:
    def __init__(self, x=0, y=0, z=0, w=0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.w = float(w)

    def __repr__(self) -> str:
        return f'Tuple({self.x!r}, {self.y!r}, {self.z!r}, {self.w!r})'

    def __eq__(self, other):
        def eqval(m, n):
            EPSILON = 1e-6
            return abs(m - n) < EPSILON

        if isinstance(other, Tuple):
            return (
                eqval(self.x, other.x)
                and eqval(self.y, other.y)
                and eqval(self.z, other.z)
                and eqval(self.w, other.w)
            )
        else:
            return NotImplemented


class Point:
    def __init__(self, x=0, y=0, z=0):
        self.p = Tuple(x, y, z, 1.0)

    def __repr__(self) -> str:
        return f'Point({self.p.x!r}, {self.p.y!r}, {self.p.z!r})'

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.p == other.p
        elif isinstance(other, Tuple):
            return self.p == other
        else:
            return NotImplemented


class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.v = Tuple(x, y, z, 0.0)

    def __repr__(self) -> str:
        return f'Vector({self.v.x!r}, {self.v.y!r}, {self.v.z!r})'

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.v == other.v
        elif isinstance(other, Tuple):
            return self.v == other
        else:
            return NotImplemented
