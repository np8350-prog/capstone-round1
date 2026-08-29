import pandas as pd

df = pd.read_excel('AIID_Excel_Export.xlsx', skiprows=2)

for col in ['AI Harm Level', 'Intentional Harm', 'Rights Violation']:
    print('---', col, '---')
    print(df[col].value_counts(dropna=False).head(12))
    print()
