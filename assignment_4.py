"""
Assignment 4 GTECH 731 Spring 2022

Daniel Vignoles
"""

import geopandas as gpd
import matplotlib.pyplot as plt
from pathlib import Path


def df_from_pluto(pluto, to_crs='EPSG:32618'):
    """Read into geopandas assuming source is epsg:4326.
       to_crs defaults to UTM Zone 18."""

    df = gpd.read_file(pluto)
    assert df.crs.srs.lower() == 'epsg:4326'
    df.to_crs(to_crs, inplace=True)

    return df


def main():
    pluto_astoria = Path(__file__).parent.joinpath("inputs/pluto.geojson")
    pluto_lic = Path(__file__).parent.joinpath("inputs/pluto-LIC.geojson")

    df_astoria = df_from_pluto(pluto_astoria)
    df_lic = df_from_pluto(pluto_lic)

    print(f"Pluto Astoria Building Area Mean: {df_astoria.bldgarea.mean()} m^2")
    print(f"Pluto LIC Building Area Mean: {df_lic.bldgarea.mean()} m^2")

    # Long Island State Plane
    df_astoria_2263 = df_astoria.to_crs('EPSG:2263')

    fig, axes = plt.subplots(nrows=2)

    df_astoria.plot(ax=axes[0])
    axes[0].set_title('Astoria Pluto UTM Zone 18')

    df_astoria_2263.plot(ax=axes[1])
    axes[1].set_title('Astoria Pluto Long Island State Plane')
    fig.tight_layout()

    png = "Astoria-Pluto.png"
    plt.savefig(png, dpi=100, format="png")
    print(f"plot saved as {png}")

    # convert meters squared to ft squared
    M2_TO_FT2 = 10.7639

    fig2, ax = plt.subplots()

    utm_area = df_astoria.area *  M2_TO_FT2
    lisp_area = df_astoria_2263.area
    ax.plot(utm_area, lisp_area)
    ax.set_title('Astoria Building Area')
    ax.set_xlabel('UTM Z 18 N')
    ax.set_ylabel('Long Island State Plane')
    fig.tight_layout()

    png = "crs-area-comparison.png"
    plt.savefig(png, dpi=100, format="png")
    print(f"plot saved as {png}")

    print('Astoria Pluto Building Area UTM Z18 N')
    print(utm_area.describe())

    print('Astoria Pluto Building Area Long Island State Plane')
    print(lisp_area.describe())

    plt.show()

if __name__ == "__main__":
    main()
