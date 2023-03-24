import xarray as xr
import pandas as pd

# load the .nc file
ds = xr.open_dataset('dataverse_files/SO2_London_Paris.nc')

# convert the file to a pandas DataFrame
df = ds.to_dataframe()

# convert the DataFrame to a JSON object
json_data = df.to_json(orient='split', indent=4)

# write the JSON object to a file
with open('SO2_London_Paris.json', 'w') as f:
    f.write(json_data)
