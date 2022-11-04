import pandas as pd
import json
# This script splits the test from the excel to get the data we need

with open(r'paths.json') as d:
    paths = json.load(d)['Unzip'][0]

df = pd.read_excel(paths['ac_simulationexcel'])
df.rename(columns={'V(fb+-1)':'vout'}, inplace=True)
df['vout'] = df['vout'].str.split('(', expand=True)[1]
df['vout'] = df['vout'].str.split('d', expand=True)[0]
df['vout'] = '=VALUE(' + df['vout'] + ')'
df.to_excel(paths['ac_simulationexceledit'])

read_file = pd.read_csv(paths['nimble_excel_path'])
read_file.to_excel(paths['transfer_function'], index = None, header=True)