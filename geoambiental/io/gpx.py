import gpxpy

from ..PointArray import PointArray


def read_gpx_waypoints(path: str) -> PointArray:
    """
    Lee un archivo gpx y regresa un geoambiental.PointArray con todos los
    waypoints que contiene el archivo

    Parámetros
    ----------
    `path : str`
        Dirección del archivo gpx de donde se obtendrán los datos

    Notas
    -----
    None

    Ejemplos
    --------
    Leer un archivo gpx:
    >>> puntos_madrigueras = read_gpx_waypoints('direccion_archivo_gpx.gpx')
    Para graficar la colección de polígonos que se cargan se puede usar:
    >>> plt.plot(puntos_madrigueras.lon, puntos_madrigueras.lat)
    """
    with open(path, "r") as gpx_file:
        gpx = gpxpy.parse(gpx_file)
    lon = [point.longitude for point in gpx.waypoints]
    lat = [point.latitude for point in gpx.waypoints]
    return PointArray(lat, lon)
