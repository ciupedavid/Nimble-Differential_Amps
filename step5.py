import pandas as pd

# Split the text

df = pd.read_excel(r"C:\Users\davciupe\Downloads\AC_simulation.xlsx")
df.rename(columns={'V(fb+-1)':'vout'}, inplace=True)
df['vout'] = df['vout'].str.split('(', expand=True)[1]
df['vout'] = df['vout'].str.split('d', expand=True)[0]
df['vout'] = '=VALUE(' + df['vout'] + ')'
df.to_excel(r"C:\Users\davciupe\Downloads\AC_simulationEdit.xlsx")

read_file = pd.read_csv(r'C:\Users\davciupe\Downloads\Raw Data\Individual Stage Data\Amplifier\Amplifier - Transfer Function.csv')
read_file.to_excel(r'C:\Users\davciupe\Downloads\Transfer Function.xlsx', index = None, header=True)