# Data for DS Project

## TLDR

First, go to [Replication Data for: Paintings by Turner and Monet Depict Trends in 19th Century Air Pollution - Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/YQOLZW), select all files, download zip, and unzip the `dataverse_files` folder. Then, put the `dataverse_files` folder in the root directory of this repo.

- All data (contrast, saturation, brightness, dominant_hue, category) for every single painting: `data/contrast.json`
- SO2 levels, London & Paris: `data/so2.json`
- Suspended Particulate Matter (SPM), London: `data/london-spm.csv`
- UK coal output: `data/coal-output.csv`
- UK total energy consumption: `data/energy-output.csv`

## Some notes

- For `data/contrast.json`:
  - All values are not normalized. The range for contrast, saturation, and brightness is 0-255. The range for dominant_hue is 0-360.
  - Maybe ignore dominant_hue for now? I don't expect it to be related to air pollution in the current form.
  - Category is 1 for clear, 2 for cloudy, 3 for dawn/dusk.
  - Includes location.
- For `data/so2.json`:
  - Taken from paper, includes data for London and Paris.
  - Simulated.
- For `data/london-spm.csv`:
  - Simulated.
  - Despite having one data per year, the data quality is not very good, seems like a linear interpolation between a few data points.
  - Only have data for London.
- For `data/coal-output.csv`:
  - Incomplete, 5 coal output data points from 1853 to 1903, only 3 coal industry employment data points from 1853 to 1903.
- For `data/energy-output.csv`:
  - Complete data every 10 years from 1800 to 1900.
  - Index assumes 1800 is 100.

## Examples

See `plot.ipynb` for examples.
