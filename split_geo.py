

import json
import sys


data_file = sys.argv[1]  #original file
save_folder = sys.argv[2]  #parsed/destination

json_data = open(data_file, 'r')
data = json.load(json_data)

# Define the out data dict. We want crs & type to
# stay the same, so we will go ahea and store those.
feature = {}

#[u'geometry', u'type', u'properties']
count = 0
for f in data['features']:
	if count < 1:
		nbhd_id = f['properties']['NBHD']
		nbhd_name = f['properties']['NEIGHBORHO']
		file_name = nbhd_name.replace(' ','-').lower() + '-' + nbhd_id

		feature['geometry'] = f['geometry']
		feature['type'] = f['type']
		feature['properties'] = f['properties']
	count+=1

	out_file = save_folder + file_name + '.geojson'
	with open(out_file, 'wb') as fp:
	    json.dump(feature, fp)

