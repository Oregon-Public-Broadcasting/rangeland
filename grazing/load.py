import os
from django.contrib.gis.utils import LayerMapping

# Auto-generated `LayerMapping` dictionary for TsunamiZone model,
# modified later by cool devs.
boundary_mapping = {
    #'allotment': 'id', # layermapping and foreignkeys are mucking it up, we'll fill this in later ...
    'allotment_name': 'ALLOT_NAME',
    'allotment_unique': 'allot_uniq',
    'state': 'ADMIN_ST',
    'geom': 'POLYGON',
}

boundary_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/boundaries/allotments_plus_difference_minus_duplicates.shp'))

def run(verbose=True):
    "Loading allotment boundary shapefile into models"

    from .models import Boundary
    lm3 = LayerMapping(Boundary, boundary_shp, boundary_mapping,
                       transform=True, encoding='iso-8859-1')#,
                       #unique=['allot_uniq'])
    lm3.save(strict=True, verbose=verbose)
