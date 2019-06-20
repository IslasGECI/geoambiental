from matplotlib import path

from ..interfaces.IGeoReference import IGeoReference
from ..interfaces.IGeoReferenceBounded import IGeoReferenceBounded


def in_polygon(polygon: IGeoReferenceBounded, geo_reference: IGeoReference):
    es_dentro = []
    poligono = path.Path(
        [coordenada for coordenada in zip(polygon.lon, polygon.lat)])
    for lon, lat in zip(geo_reference.lon, geo_reference.lat):
        es_dentro.append(poligono.contains_points([(lon, lat)])[0])
    return es_dentro
