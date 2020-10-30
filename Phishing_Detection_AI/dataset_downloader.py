# Getting phishtank data
import wget
from datetime import datetime
from os import listdir
from os.path import isfile, join
import pandas as pd

dataset_folder = "online_valid_datasets"
url = 'http://data.phishtank.com/data/online-valid.csv'
current_data = datetime.today().strftime('%Y-%m-%d')
new_index = len([f for f in listdir(dataset_folder) if "online-valid" in f and current_data in f])+1
download_filename = f"online-valid_{current_data}_{new_index}.csv"
wget.download(url, join(dataset_folder, download_filename))

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

online_valid_df.to_csv("combined_online_valid.csv")