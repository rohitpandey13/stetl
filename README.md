# Stetl - Streaming ETL

Stetl, streaming ETL, pronounced "staedl", is a lightweight [FOSS](LICENSE.txt) ETL-framework for geospatial data conversion. 

## Documentation

The Stetl website and documentation can be found via http://stetl.org.
For a quick overview read the [5-minute Stetl-introduction](http://www.slideshare.net/justb4/5-minute-intro-to-setl),  
or a [more detailed presentation](http://www.slideshare.net/justb4/stetl-foss4g20131024v1).
Stetl was presented at several events like the
[FOSS4G 2013 in Nottingham](http://2013.foss4g.org) and (the upcoming) [GeoPython 2016](http://www.geopython.net).

## Concepts 

Stetl basically glues together existing parsing and transformation tools like [GDAL/OGR](http://gdal.org), Jinja2 and XSLT.
By using native tools like libxml and libxslt (via Python lxml) Stetl is speed-optimized.

A configuration file, in Python config `.ini` format, specifies a chained sequence of transformation 
steps: typically an `Input` connected to one or more `Filters`, and finally an `Output`.
At runtime, this sequence is realized by a series of Python modules/objects. These are 
symbolically specified and parameterized in the config file. 
Via the `stetl -c <config file>`  command, the transformation is executed.

Stetl has been proven to handle 10's of millions of objects without any memory issues.
This is achieved through a technique called "streaming and splitting". 
For example: using the `OgrPostgisInput` module an GML stream can be generated from the database.
A component called the `GmlSplitter` can split this stream into manageable chunks (like 20000 features) 
and feed this upstream into the ETL chain.

## Use Cases

Stetl has been found particularly useful for complex GML-related ETL-cases, like those found
within [EU INSPIRE](http://inspire.ec.europa.eu/) Data Harmonization and the transformation
of GML/XML-based National geo-datasets to for example PostGIS.

Most of the data conversions within the [Dutch NLExtract Project](https://github.com/opengeogroep/NLExtract) apply Stetl.

Stetl also proved to be very effective in [IoT-related transformations involving the SensorWeb/SOS](https://github.com/Geonovum/smartemission).

## Examples

Browse all examples under the [examples dir](examples). 
Best is to start with the [basic examples](examples/basics)

## Installation
 
Stetl can be installed via PyPi `pip install stetl` and recently as a [Stetl Docker image](https://hub.docker.com/r/justb4/stetl).
More on [installation in the documentation](http://www.stetl.org/en/latest/install.html).

## Contributing

Anyone and everyone is welcome to contribute. Please take a moment to
review the [guidelines for contributing](CONTRIBUTING.md).

* [Bug reports](CONTRIBUTING.md#bugs)
* [Feature requests](CONTRIBUTING.md#features)
* [Pull requests](CONTRIBUTING.md#pull-requests)

## Origins

Stetl originated in the INSPIRE-FOSS project ([2009-2013 now archived](https://github.com/justb4/inspire-foss). 
Since then Stetl evolved into a wider use like
transforming [Dutch GML-based Open Datasets](https://github.com/opengeogroep/NLExtract) such as IMGEO/BGT (Large Scale Topography) 
and IMKAD/BRK (Cadastral Data).

## Finally

The word "stetl" is also an alternative writing for "shtetl":
http://en.wikipedia.org/wiki/Stetl : "...Material things were neither disdained nor
extremely praised in the shtetl. Learning and education were the ultimate measures of 
worth in the eyes of the community,
while money was secondary to status..."



