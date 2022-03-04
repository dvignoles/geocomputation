class Point:
    def __init__(self, x, y):
        ##Assign properties
        self.x = x
        self.y = y

    def __eq__(self, other):
        if (self.x == other.x) and (self.y == other.y):
            return True
        else:
            return False

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def euclid_distance(self, p2):
        summand_1 = (p2.x - self.x) ** 2
        summand_2 = (p2.y - self.y) ** 2
        return (summand_1 + summand_2) ** (1 / 2)

    def wkt(self):
        return f"POINT ({self.x} {self.y})"


class Line:
    def __init__(self, points):
        self.points = points

    def __str__(self):
        return [p.__str__() for p in self.points].__str__()

    def get_point(self, index):
        return self.points[index]

    def wkt(self):
        # string indexing on point wkt method
        inner = ", ".join([p.wkt()[7:-1] for p in self.points])
        return f"LINESTRING ({inner})"


class Polygon(Line):
    def __init__(self, points):
        super().__init__(points)

    def is_valid(self):
        return True if self.points[0] == self.points[-1] else False

    def wkt(self):
        # string indexing of line.wkt
        inner_wkt = super().wkt()[11:]
        return f"POLYGON ({inner_wkt})"


class GeometryCollection:
    def __init__(self, geometries):
        self.points = []
        self.polygons = []
        for g in geometries:
            if isinstance(g, Point):
                self.points.append(g)
            elif isinstance(g, Polygon):
                self.polygons.append(g)

    def plot_points(self, ax, **plot_kwargs):
        for p in self.points:
            ax.plot(p.x, p.y, **plot_kwargs)

    def plot_polygons(self, ax, **plot_kwargs):
        for pol in self.polygons:
            x = [p.x for p in pol.points]
            y = [p.y for p in pol.points]

            ax.plot(x, y, **plot_kwargs)

    def plot(self, ax, **plot_kwargs):
        self.plot_points(ax, **plot_kwargs)
        self.plot_polygons(ax, **plot_kwargs)


if __name__ == "__main__":
    p1 = Point(3, 4)
    p2 = Point(7, 9)
    p3 = Point(4, 33)
    p4 = Point(7, 9)

    print(p1.euclid_distance(p2))
    print(p2.euclid_distance(p3))
    print(p2 == p4)
    print(p1 == p3)

    l1 = Line([p1, p2, p3])
    poly_1 = Polygon([p2, p1, p3, p4])
    poly_2 = Polygon([p1, p2, p3, p4])

    print(poly_1.is_valid())
    print(poly_2.is_valid())
    print(l1)
    print(p1.wkt())
    print(l1.wkt())
    print(poly_1.wkt())
