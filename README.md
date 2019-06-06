Clases para manipular y cargar datos geoambientales
====

[![Build Status](https://travis-ci.org/IslasGECI/geoambiental.svg?branch=feature%2Fagrega_soporte_travis)](https://travis-ci.org/IslasGECI/geoambiental)

El repositorio *geoambiental* contiene las clases `Map`, `Field`, `TimeSeries` y `Profile`. Las clases definidas en este repositorio se usan para comunicar la capa _procesamiento_ (_negocio_) con la capa _graficado_ (_presentación_). La salida de las funciones en la capa de _procesamiento_ son objetos que pertenecen a las clases de este repositorio y a su vez son la entrada de las funciones en la capa de _graficado_.

## Diagrama UML

### Estado actual
![uml](/referencias/uml-geoambiental-actual.svg)

### Estado deseado
![uml](/referencias/uml-geoambiental-deseado.svg)