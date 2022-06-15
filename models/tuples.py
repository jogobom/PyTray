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
            return abs(m - n) < 1e-6

        if isinstance(other, Tuple):
            return (
                eqval(self.x, other.x)
                and eqval(self.y, other.y)
                and eqval(self.z, other.z)
                and eqval(self.w, other.w)
            )
        return NotImplemented


class Point:
    def __init__(self, x=0, y=0, z=0):
        self.point = Tuple(x, y, z, 1.0)

    def __repr__(self) -> str:
        return f'Point({self.point.x!r}, {self.point.y!r}, {self.point.z!r})'

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.point == other.point
        if isinstance(other, Tuple):
            return self.point == other
        return NotImplemented


class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.vector = Tuple(x, y, z, 0.0)

    def __repr__(self) -> str:
        return (
            f'Vector({self.vector.x!r}, {self.vector.y!r}, {self.vector.z!r})'
        )

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.vector == other.vector
        if isinstance(other, Tuple):
            return self.vector == other
        return NotImplemented
