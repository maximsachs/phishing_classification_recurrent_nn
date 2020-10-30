import wget
from datetime import datetime
from os import listdir
from os.path import isfile, join
import pandas as pd

# Settings:
dataset_folder = "online_valid_datasets"
url = 'http://data.phishtank.com/data/online-valid.csv'

# Saving files in format: "online-valid_YYYY-mm-dd_i.csv"
current_data = datetime.today().strftime('%Y-%m-%d')
# Counting the number of docs already downloaded for today:
new_index = len([f for f in listdir(dataset_folder) if "online-valid" in f and current_data in f])+1
download_filename = f"online-valid_{current_data}_{new_index}.csv"
# Getting the current dataset and saving it with the new filename
wget.download(url, join(dataset_folder, download_filename))

# Iterating over all files in the dataset and combining them into one big one.
# Merging on the phish_id column, which is considered unique per url.
online_valid_df = pd.DataFrame()
for f in listdir(dataset_folder):
    f_path = join(dataset_folder, f)
    if isfile(f_path) and "online-valid" in f and ".csv" in f:
        if online_valid_df.empty:
            online_valid_df = pd.read_csv(f_path)
            online_valid_df.set_index("phish_id", inplace=True)
        else:
            online_valid_df_new = pd.read_csv(f_path)
            online_valid_df_new.set_index("phish_id", inplace=True)
            online_valid_df = online_valid_df.merge(online_valid_df_new, how="outer")

# Saving the combined dataframe to file for posterity.
online_valid_df.to_csv("combined_online_valid.csv")
print("Done")