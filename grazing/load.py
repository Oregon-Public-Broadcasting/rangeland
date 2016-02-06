import os
from django.contrib.gis.utils import LayerMapping

# Auto-generated `LayerMapping` dictionary for TsunamiZone model,
# modified later by cool devs.
boundary_mapping = {
    #'allotment': 'id', # layermapping and foreignkeys are mucking it up, we'll fill this in later ...

    'allotment_name': 'ALLOT_NAME',
    'allotment_unique': 'STALLOT',
    # 'state': 'ADMIN_ST',
    'geom': 'POLYGON',
    'lhs2007': 'LHS_2007',
    'lhs2012': 'LHS_2012',
    'lhs': 'LHS_CLASS',
    'ecoregion1': 'ECO_I',
    'ecoregion2': 'ECO_II',
    'ecoregion3': 'ECO_III'
}

boundary_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/boundaries/BLM_LHSdataV4_02012016a.shp'))

def run(verbose=True):
    "Loading allotment boundary shapefile into models"

    from .models import Health
    lm3 = LayerMapping(Health, boundary_shp, boundary_mapping,
                       transform=True, encoding='iso-8859-1')#,
                       #unique=['allot_uniq'])
    lm3.save(strict=True, verbose=verbose)
