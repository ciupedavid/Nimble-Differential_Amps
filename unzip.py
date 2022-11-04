# This script Unzips the downloaded file from the script1

import zipfile
import json


with open(r'paths.json') as d:
    paths = json.load(d)['Unzip'][0]

# Unzip files
# print(paths)
with zipfile.ZipFile(paths['LTspice_path']) as zip_ref:
     zip_ref.extractall(paths['extract_path'])

with zipfile.ZipFile(paths['nimble_path']) as zip_ref:
    zip_ref.extractall(paths['extract_path'])
