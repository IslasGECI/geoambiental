from matplotlib import path

from ..interfaces.IGeoReference import IGeoReference
from ..interfaces.IGeoReferenceBounded import IGeoReferenceBounded


def in_polygon(geo_element: IGeoReference, polygon: IGeoReferenceBounded):
    es_dentro = []
    poligono = path.Path([coordenada for coordenada in zip(polygon.lon, polygon.lat)])
    for lon, lat in zip(geo_element.lon, geo_element.lat):
        es_dentro.append(poligono.contains_points([(lon, lat)])[0])
    return es_dentro
