from geocomp.shapes import Point, Line, Polygon

if __name__ == '__main__':
    p1 = Point(3,4)
    p2 = Point(7,9)
    p3 = Point(4,33)
    p4 = Point(7,9)

    print(p1.euclid_distance(p2))
    print(p2.euclid_distance(p3))
    print(p2 == p4)
    print(p1 == p3)

    l1 = Line([p1,p2,p3])
    poly_1 = Polygon([p2,p1,p3,p4])
    poly_2 = Polygon([p1,p2,p3,p4])

    print(poly_1.is_valid())
    print(poly_2.is_valid())
    print(l1)
    print(p1.wkt())
    print(l1.wkt())
    print(poly_1.wkt())
