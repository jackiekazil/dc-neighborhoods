"""
	This file splits a geojson that is a feature collection into invdividual feature files.
	The first arg passed is the location of the feature collection geojson.
	The second arg pass is the folder where the individuals features will be written to.
"""

import json
import sys

from slugify import slugify


data_file = sys.argv[1]  #original file
save_folder = sys.argv[2]  #parsed/destination

json_data = open(data_file, 'r')
data = json.load(json_data)

# Define the out data dict. We want crs & type to
# stay the same, so we will go ahea and store those.
feature = {}

for f in data['features']:
	nbhd_id = f['properties']['NBHD']
	nbhd_name = slugify(f['properties']['NEIGHBORHO'])
	file_name = nbhd_name + '-' + nbhd_id

	feature['geometry'] = f['geometry']
	feature['type'] = f['type']
	feature['properties'] = f['properties']

	out_file = save_folder + file_name + '.geojson'
	with open(out_file, 'wb') as fp:
	    json.dump(feature, fp)