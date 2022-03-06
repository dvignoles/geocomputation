"""
Assignment 3 GTECH 731 Spring 2022

Daniel Vignoles
"""

import json
import matplotlib.pyplot as plt

from geocomp.shapes import Point, Polygon, GeometryCollection


def process_geojson(geojson):
    with open(geojson, "r") as f:
        data = f.read()
        pluto = json.loads(data)
        buildings = {}
        polygons = []
        for feature in pluto["features"]:
            bldgarea = feature["properties"]["bldgarea"]
            lotarea = feature["properties"]["lotarea"]
            ratio = bldgarea / lotarea if lotarea > 0 else "NA"
            buildings[feature["properties"]["bbl"]] = {
                "bldgarea": bldgarea,
                "lotarea": lotarea,
                "bldgarea:lotarea": ratio,
            }
            coords = feature["geometry"]["coordinates"][0][0]
            points = [Point(p[0], p[1]) for p in coords]
            polygons.append(Polygon(points))

    return buildings, polygons


def demo_geom_collection():
    p1 = Point(4, 5)
    p2 = Point(4, 8)
    p3 = Point(11, 4)
    p4 = Point(9, 12)
    p5 = Point(14, 9)
    p6 = Point(4, 16)
    p7 = Point(17, 7)

    poly1 = Polygon([p1, p2, p3, p1])
    poly2 = Polygon([p5, p4, p3, p5])

    collection = GeometryCollection([p6, p7, poly1, poly2])
    fig, ax = plt.subplots()
    collection.plot(ax, marker="o", markersize=20)

    return fig, ax


def main():
    buildings, polygons = process_geojson("inputs/pluto.geojson")
    print(f"A building: {buildings[4003140001]}")
    print(f"A polygon: {polygons[0]}")

    fig, ax = demo_geom_collection()
    png = "GeometryCollection.png"
    plt.savefig(png, dpi=100, format="png")
    print(f"GeometryCollection plot saved as {png}")


if __name__ == "__main__":
    main()
