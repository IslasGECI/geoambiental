import geopy.distance

from ..Point import Point


def distance_between_points_m(geopoint_from: Point, geopoint_to: Point):
    coordenada_1 = (geopoint_from.lat, geopoint_from.lon)
    coordenada_2 = (geopoint_to.lat, geopoint_to.lon)
    return geopy.distance.distance(coordenada_1, coordenada_2).m


def distance_between_points_km(geopoint_from: Point, geopoint_to: Point):
    coordenada_1 = (geopoint_from.lat, geopoint_from.lon)
    coordenada_2 = (geopoint_to.lat, geopoint_to.lon)
    return geopy.distance.distance(coordenada_1, coordenada_2).km
