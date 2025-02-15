from astroquery.mast import Observations
import pandas as pd


obs_table = Observations.query_criteria(target_name="Milky Way", obs_collection="SDSS")

if len(obs_table) > 0:
    df = obs_table.to_pandas()

    print(df.columns) 
    print(df.head())   
else:
    print("No data found for Milky Way in the HST collection.")
