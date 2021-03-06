from setuptools import setup, find_packages

setup(
    name="geoambiental",
    version="0.1.0",
    packages=find_packages(),
    install_requires = [
        "geoarea",
        "geopandas",
        "geopy",
        "gpxpy",
        "matplotlib",
        "numpy",
        "scipy",
        "sklearn",
        "utm"
    ]
)
