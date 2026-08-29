import pandas as pd

df = pd.read_excel('AIID_Excel_Export.xlsx', skiprows=2)

for col in ['Harm Domain', 'Tangible Harm', 'Risk Domain', 'Risk Subdomain', 'Harm Distribution Basis']:
    print('---', col, '---')
    print(df[col].value_counts(dropna=False).head(12))
    print()
