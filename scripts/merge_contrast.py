import json

with open('data/turner_contrast.json') as f:
    turner_data = json.load(f)

# Add "London" as the location for all Turner paintings
for i in range(len(turner_data)):
    turner_data[i]['Location'] = 'London'

with open('data/monet_contrast.json') as f:
    monet_data = json.load(f)

# Renumber the Monet paintings
for i in range(len(monet_data)):
    monet_data[i]['No.'] = str(int(monet_data[i]['No.']) + len(turner_data))

# Merge the data
merged_data = turner_data + monet_data

# Convert years from strings to numbers
for i in range(len(merged_data)):
    if '-' in merged_data[i]['Year']:
        merged_data[i]['Year'] = int(merged_data[i]['Year'].split('-')[0])
    else:
        merged_data[i]['Year'] = int(merged_data[i]['Year'])

# Save the merged data to a new file
with open('data/merged_contrast.json', 'w') as f:
    json.dump(merged_data, f, indent=4)
