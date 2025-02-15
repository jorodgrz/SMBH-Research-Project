from astroquery.mast import Observations

obs_table = Observations.query_criteria(target_name="M31", obs_collection="HST")


print(obs_table)


import pandas as pd
df = obs_table.to_pandas()
print(df.head())

print(df.columns)  

metallicity_data = df['metallicity_column_name']
print(metallicity_data)

import matplotlib.pyplot as plt

plt.plot(df['metallicity_column_name'], 'o')
plt.title("Metallicity of M31 Stars")
plt.xlabel("Index")
plt.ylabel("Metallicity")
plt.show()

