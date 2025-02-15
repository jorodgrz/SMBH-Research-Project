from astroquery.mast import Observations
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

print("Querying MAST for M31 observations from JWST...")
observations = Observations.query_criteria(
    target_name="M31",
    project="JWST",
    dataproduct_type="spectrum"
)

print(f"Found {len(observations)} observations.")
if len(observations) > 0:
    print(observations[['obs_id', 'target_name', 'obs_collection', 'instrument_name']])

obs_id = observations[0]['obs_id'] 
print(f"Fetching data products for observation ID: {obs_id}")
data_products = Observations.get_product_list(obs_id)


filtered_products = Observations.filter_products(data_products, productSubGroupDescription="CAL")
downloaded_files = Observations.download_products(filtered_products, download_dir="./data/")

#extract metallicity
fits_file = downloaded_files['Local Path'][0]  
print(f"Reading FITS file: {fits_file}")
hdul = fits.open(fits_file)

hdul.info()

data = hdul[1].data 
columns = data.columns
print("Available columns:", columns)


metallicity = data['metallicity_column_name']  
hdul.close()

# Plot metallicity distribution
plt.figure(figsize=(10, 6))
plt.hist(metallicity, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.title("Metallicity Distribution in M31 Stars (JWST)", fontsize=14)
plt.xlabel("Metallicity", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.grid(axis='y', alpha=0.75)
plt.show()

