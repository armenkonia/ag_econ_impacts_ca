# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:02:06 2024

@author: armen
"""

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import fiona

#%%
sac_id = gpd.read_file(r"C:\Users\armen\Desktop\COEQWAL\Datasets\ppic-sacramento-valley-delta-surface-water-availability\PPIC_SacramentoValley_SW_Availability_Shapes\ppic-sacramentovalley-sw-availability.shp")
sj_id = gpd.read_file(r"C:\Users\armen\Desktop\COEQWAL\Datasets\ppic-san-joaquin-valley-surface-water-availability\ppic_sjv_sw_availability.shp")

sac_id = sac_id.to_crs(epsg=3310)
sj_id = sj_id.to_crs(epsg=3310)

sj_id = sj_id.drop(columns=['OBJECTID_1'])
sac_id = sac_id.rename(columns={'AGENCYNAME': 'Agency_Nam',})
sac_id = sac_id.loc[:, ['Agency_Nam', 'geometry','gross_serv']]
sj_id = sj_id.loc[:, ['Agency_Nam', 'geometry','Service_Ar']]
sac_id = sac_id.rename(columns={'gross_serv': 'Total area',})
sj_id = sj_id.rename(columns={'Service_Ar': 'Total area',})
cv_id = pd.concat([sj_id, sac_id])

gdb_path = r"C:\Users\armen\Documents\ArcGIS\Projects\COEQWAL\COEQWAL.gdb"
cv_id.to_file(gdb_path, layer='central_valley_irrigation_districts', driver="GPKG")

# sjoin is good if you want to intersect points with polygons, not polygon with polygons 