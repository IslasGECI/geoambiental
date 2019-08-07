from __future__ import annotations

import numpy as np

from .interfaces import IGeoReference, ITimeReference, IGeoReferenceFinite
from .Line import Line


class Trajectory(Line, ITimeReference):

    def __init__(self, lat, lon, date):
        super().__init__(lat, lon)
        self._date = np.array(date)

    def __getitem__(self, index) -> Trajectory:
        linea = super().__getitem__(index)
        fechas = self._date[index]
        return Trajectory(linea.lat, linea.lon, fechas)

    @property
    def date(self) -> np.array:
        return np.array(self._date)
