# This script Unzips the downloaded file from the script1
import time
import zipfile
import json
import shutil
import os

with open(r'inAMPNoise.json') as d:
    paths = json.load(d)['Nimble'][0]

project_location = paths['project_location']
device = paths['device']
gain = paths['gain']

# Unzip files
# print(paths)
unzip_path_ltspice = project_location + '\\' + device + '\\' + 'LTspice - ' + device + ' G' + gain + '.zip'
print(unzip_path_ltspice)
with zipfile.ZipFile(unzip_path_ltspice) as zip_ref:
    new_path = project_location + '\\' + device
    print(new_path)
    zip_ref.extractall(new_path)

unzip_path_nimble = project_location + '\\' + device + '\\' + 'Nimble - ' + device + ' G' + gain + '.zip'
print(unzip_path_nimble)
with zipfile.ZipFile(unzip_path_nimble) as zip_ref:
    zip_ref.extractall(new_path)

time.sleep(1)
raw_data = project_location + '\\' + device + '\\' + 'Raw Data' + '\\' + 'Individual Stage Data' + '\\' + 'Amplifier' + '\\' + 'Amplifier - Output Referred Noise.csv'
shutil.move(raw_data, project_location + device)

time.sleep(1)

# extra_files_remove = paths['project_location'] + paths['device']
# shutil.rmtree(extra_files_remove + '\\' + 'Raw Data')
# os.rmdir(extra_files_remove + '\\' + 'Raw Data')