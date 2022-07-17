# docker-compose run --rm app python3 utils/read_json.py
import json

f = open('utils/brazil-states.geojson')
data = json.load(f)
result = {}
for i in data['features']:
    name = i['properties']['name']
    polygon = i['geometry']['coordinates'][0][0]
    polygon = [x[::-1] for x in polygon]
    result[name] = polygon
f.close()

with open('utils/mock.json', 'w') as f:
    json.dump(result, f)
