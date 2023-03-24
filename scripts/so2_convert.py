import json

# load the JSON data from file
with open('SO2_London_Paris.json', 'r') as f:
    json_data = json.load(f)

# loop through the index and data arrays and create a new dictionary for each row of data
rows = []
for i, index_data in enumerate(json_data['index']):
    row = {'year': index_data['year']}
    for j, column in enumerate(json_data['columns']):
        row[column] = json_data['data'][i][j]
    rows.append(row)

# write the new JSON object to a file
with open('SO2_London_Paris_new.json', 'w') as f:
    json.dump(rows, f, indent=2)
