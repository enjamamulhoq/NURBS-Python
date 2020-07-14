""" GEOMDL - Object-oriented, self-contained, pure Python B-Spline and NURBS library

.. moduleauthor:: Onur R. Bingol <contact@onurbingol.net>
.. moduleauthor:: The GEOMDL Contributors

"""

# Library version
__version__ = "6.0a1"

# Author and license
__author__ = "Onur R. Bingol"
__license__ = "MIT"

# Optional variables
__description__ = 'Object-oriented B-Spline and NURBS library'
__keywords__ = 'NURBS B-Spline curve surface volume computational-geometry CAD modeling visualization'

# Support for "from geomdl import *"
# @see: https://stackoverflow.com/a/41895257
# @see: https://stackoverflow.com/a/35710527
__all__ = [
    'BSpline',
    'NURBS',
    'freeform',
    'knotvector',
    'helpers',
    'evaluators',
    'algorithms',
    'fitting',
    'geomutils',
    'tessellate',
    'voxelate',
    'exchange',
    'entity',
    'ray',
    'linalg',
    'utilities'
]

# Register default types for isinstance() checking
from .base import GeomdlTypeSequence, GeomdlTypeString
from .base import GeomdlList

# Default types for sequences
GeomdlTypeSequence.register(list)
GeomdlTypeSequence.register(tuple)
GeomdlTypeSequence.register(GeomdlList)

# Default types for strings
GeomdlTypeString.register(str)


def geomdl_version():
    """ Returns geomdl full version as a tuple """
    return tuple(__version__.split('.'))
