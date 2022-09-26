import zipfile

# Unzip files

with zipfile.ZipFile(r'C:\Users\davciupe\Downloads\LTspice September 14, 2022.zip') as zip_ref:
     zip_ref.extractall(r'C:\Users\davciupe\Downloads')

with zipfile.ZipFile(r'C:\Users\davciupe\Downloads\Raw Data Export - September 14, 2022.zip') as zip_ref:
    zip_ref.extractall(r'C:\Users\davciupe\Downloads')