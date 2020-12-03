import numpy as np
from sklearn.datasets.species_distributions import construct_grids
from sklearn.neighbors import KernelDensity

from .interfaces import IGeoReference


def get_kernel_density_geographic(
    GeoreferenceObject: IGeoReference, bandwidth=0.005, xbins=100, ybins=100, **kwargs
):
    x = np.linspace(
        GeoreferenceObject.lon.min() - bandwidth * 2,
        GeoreferenceObject.lon.max() + bandwidth * 2,
        xbins,
    )
    y = np.linspace(
        GeoreferenceObject.lat.min() - bandwidth * 2,
        GeoreferenceObject.lat.max() + bandwidth * 2,
        ybins,
    )
    xgrid, ygrid = np.meshgrid(x, y)
    xy_sample = np.vstack([ygrid.ravel(), xgrid.ravel()]).T
    xy_train = np.vstack([GeoreferenceObject.lat, GeoreferenceObject.lon]).T
    xy_sample = np.radians(xy_sample)
    xy_train = np.radians(xy_train)
    kde = KernelDensity(bandwidth=bandwidth, metric="haversine")
    kde.fit(xy_train)
    Z = np.exp(kde.score_samples(xy_sample))
    Z = Z.reshape(xgrid.shape)
    return xgrid, ygrid, Z


def get_kernel_density(
    GeoreferenceObject: IGeoReference, bandwidth=0.005, xbins=100, ybins=100, **kwargs
):
    x = np.linspace(
        GeoreferenceObject.x.min() - bandwidth * 2,
        GeoreferenceObject.x.max() + bandwidth * 2,
        xbins,
    )
    y = np.linspace(
        GeoreferenceObject.y.min() - bandwidth * 2,
        GeoreferenceObject.y.max() + bandwidth * 2,
        ybins,
    )
    xgrid, ygrid = np.meshgrid(x, y)
    xy_sample = np.vstack([ygrid.ravel(), xgrid.ravel()]).T
    xy_train = np.vstack([GeoreferenceObject.y, GeoreferenceObject.x]).T
    kde = KernelDensity(bandwidth=bandwidth)
    kde.fit(xy_train)
    Z = np.exp(kde.score_samples(xy_sample))
    Z = Z.reshape(xgrid.shape)
    return xgrid, ygrid, Z
