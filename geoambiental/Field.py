import numpy as np
import utm

from .Grid import Grid
from .interfaces import IGeoReferenceBounded, ITimeReference
from .Map import Map
from .Point import Point


class Field(Grid, ITimeReference):
    def __init__(self, lat, lon, value, date, dimensions="lon,lat,t"):
        super(Field, self).__init__(lat, lon)
        self._date = date
        self._value = value
        self._dimensions = dimensions

    def __getitem__(self, index) -> Map:
        dimension_t = self._get_date_index_dimension()
        if dimension_t == 0:
            valor = self._value[index, :, :]
        elif dimension_t == 1:
            valor = self._value[:, index, :]
        elif dimension_t == 2:
            valor = self._value[:, :, index]
        else:
            raise Exception('No se encontró la dimensión del tiempo')
        if isinstance(index, int):
            return Map(self.lat, self.lon, valor), self.date[index]
        else:
            return Field(self.lat, self.lon, valor, self.date[index], dimensions=self._dimensions)

    @property
    def date(self):
        return self._date

    def _get_date_index_dimension(self):
        dimension_t = -1
        for i_dimension, dimension in enumerate(self._dimensions.split(",")):
            if dimension == "t":
                dimension_t = i_dimension
                break
        return dimension_t

    def set_nan_outside(self, geo_reference_bounded: IGeoReferenceBounded):
        variables = np.full(self._value.shape, np.nan)
        dimension_t = self._get_date_index_dimension()
        for i, lat in enumerate(self.lat):
            for j, lon in enumerate(self.lon):
                es_dentro = geo_reference_bounded.in_polygon(
                    Point([self.LAT[i][j]], [self.LON[i][j]]))
                if es_dentro[0]:
                    if dimension_t == 0:
                        for t, _ in enumerate(self.date):
                            variables[t][i][j] = self._value[t][i][j]
                    elif dimension_t == 1:
                        for t, _ in enumerate(self.date):
                            variables[i][t][j] = self._value[i][t][j]
                    elif dimension_t == 2:
                        for t, _ in enumerate(self.date):
                            variables[i][j][t] = self._value[i][j][t]
                    else:
                        raise Exception(
                            'No se encontró la dimensión del tiempo')
        return Field(self.lat, self.lon, variables, self.date, self._dimensions)
