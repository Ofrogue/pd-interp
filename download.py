# https://archive.ics.uci.edu/ml/datasets/Polish+companies+bankruptcy+data

# 
import os
import requests
import zipfile


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00365/data.zip"
zip_path = os.path.join("data", "data.zip")
if not os.path.isfile(zip_path):
    with open(zip_path, "wb") as f:
        print("downloading")
        req = requests.get(url=url)
        f.write(req.content)

zip_data = zipfile.ZipFile(zip_path, mode="r")

for filename in zip_data.namelist():
    save_path = os.path.join("data", filename)
    if not os.path.isfile(save_path):
        with open(save_path, 'wb') as f:
            f.write(zip_data.read(filename))

