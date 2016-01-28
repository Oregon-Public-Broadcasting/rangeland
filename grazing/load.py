import os
from django.contrib.gis.utils import LayerMapping

# Auto-generated `LayerMapping` dictionary for TsunamiZone model,
# modified later by cool devs.
boundary_mapping = {
    'allotment': 'ST_ALLOT',
    'geom': 'MULTIPOLYGON',
}

boundary_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/tsunamiZone_simple.shp'))

def run(verbose=True):
    "Loading allotment boundary shapefile into models"

    from .models import Boundary
    lm3 = LayerMapping(Boundary, boundary_shp, boundary_mapping,
                       transform=True, encoding='iso-8859-1',
                       unique=['zoneid'])
    lm3.save(strict=True, verbose=verbose)
