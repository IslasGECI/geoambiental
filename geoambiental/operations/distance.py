from scipy.spatial import distance

from ..Point import Point


def distance_between_points_m(geopoint_from: Point, geopoint_to: Point):
    distancia = distance.pdist([[geopoint_from.x, geopoint_from.y], [
                               geopoint_to.x, geopoint_to.y]], 'euclidean')
    return distancia


def distance_between_points_km(geopoint_from: Point, geopoint_to: Point):
    return distance_between_points_m(geopoint_from, geopoint_to)/1000
