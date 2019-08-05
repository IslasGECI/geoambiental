from matplotlib import path
from scipy.spatial import distance

from .IGeoReference import IGeoReference
from .IGeoReferenceBounded import IGeoReferenceBounded
from .Point import Point


def distance_between_points_m(geopoint_from: Point, geopoint_to: Point):
    distancia = distance.pdist([[geopoint_from.x, geopoint_from.y], [
                               geopoint_to.x, geopoint_to.y]], 'euclidean')
    return distancia


def distance_between_points_km(geopoint_from: Point, geopoint_to: Point):
    return distance_between_points_m(geopoint_from, geopoint_to)/1000


def in_polygon(polygon: IGeoReferenceBounded, geo_reference: IGeoReference):
    es_dentro = []
    poligono = path.Path(
        [coordenada for coordenada in zip(polygon.lon, polygon.lat)])
    for lon, lat in zip(geo_reference.lon, geo_reference.lat):
        es_dentro.append(poligono.contains_points([(lon, lat)])[0])
    return es_dentro
