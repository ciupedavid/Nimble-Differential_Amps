# This script Unzips the downloaded file from the script1

import zipfile
import json

with open(r'inAMPNoise.json') as d:
    paths = json.load(d)['Nimble'][0]

# Unzip files
# print(paths)
unzip_path = paths['ltspice'] + '\\' + paths['device'] + '\\' + 'LTspice - ' + paths['device'] + ' G10' + '.zip'
print(unzip_path)
with zipfile.ZipFile(unzip_path) as zip_ref:
    new_path = paths['ltspice'] + '\\' + paths['device']
    print(new_path)
    zip_ref.extractall(new_path)