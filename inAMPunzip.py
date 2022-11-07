# This script Unzips the downloaded file from the script1

import zipfile
import json


with open(r'inAMPNoise.json') as d:
    paths = json.load(d)['Nimble'][0]

# Unzip files
# print(paths)
with zipfile.ZipFile(paths['ltspice'] + paths['device'] + '\\' + 'LTspice - ' + paths['device'] + ' G10' + '.zip') as zip_ref:
     zip_ref.extractall(paths['ltspice'] + paths['device'])