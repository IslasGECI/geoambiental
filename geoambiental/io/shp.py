import geopandas as gp
import pandas as pd

from ..Polygon import Polygon
from ..PolygonArray import PolygonArray


def import_coast_line(path: str, projection: str = "epsg:4484") -> PolygonArray:
    """
    Importa la línea de costa y regresa un geoambiental.PolygonArray. Es importante
    especificar la proyección correcta, por _default_ utiliza la UTM11.

    Parámetros
    ----------
    `path : str`
        Dirección del archivo shp de donde se obtendrán los datos.
    `projection : str`
        Proyección epsg en la que viene el archivo shp


    Notas
    -----
    None

    Ejemplos
    --------
    Leer un archivo shp:
    >>> linea_costa_guadalupe = import_coast_line("guadalupe_LCosta.shp", projection="epsg:4484")
    """
    poligonos = gp.read_file(path)
    poligonos.crs = {"init": projection}
    poligonos_geograficas = poligonos.to_crs({"init": "epsg:4326"})
    poligonos_geograficas = multi2single(poligonos_geograficas)
    geopoligonos = []
    for i, poligono in enumerate(poligonos_geograficas.geometry):
        linea_costa = poligono.boundary
        lon = linea_costa.coords.xy[0]
        lat = linea_costa.coords.xy[1]
        geopoligonos.append(Polygon(lat, lon))
    return PolygonArray(geopoligonos)


def multi2single(gpdf):
    gpdf_singlepoly = gpdf[gpdf.geometry.type == "Polygon"]
    gpdf_multipoly = gpdf[gpdf.geometry.type == "MultiPolygon"]

    for i, row in gpdf_multipoly.iterrows():
        Series_geometries = pd.Series(row.geometry)
        df = pd.concat(
            [gp.GeoDataFrame(row, crs=gpdf_multipoly.crs).T] * len(Series_geometries),
            ignore_index=True,
        )
        df["geometry"] = Series_geometries
        gpdf_singlepoly = pd.concat([gpdf_singlepoly, df])

    gpdf_singlepoly.reset_index(inplace=True, drop=True)
    return gpdf_singlepoly
