import pandas as pd
import numpy as np

stores = pd.read_csv("testData/User.csv")
raw = pd.read_csv("testData/Client.csv")

stores["Name"] = stores["Name"].str.lower()
raw["Name"] = raw["Name"].str.lower()

def parse(name):
    try:
        row = raw[raw["Name"]==name]
        return row.iloc[0][["2022 Sales","GLA","Sales psf","Occupancy"]]
    except:
        return 0

stores[["Sales","GLA","Sales psf","Occupancy"]] = stores.apply(lambda row: parse(row["Name"]), axis=1)
stores.to_csv("data.csv")
