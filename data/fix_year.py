import pandas as pd
import ast

df = pd.read_excel('AIID_Excel_Export.xlsx', skiprows=2)

keep = [
    'Incident ID', 'date', 'year', 'Incident Year', 'title',
    'Sector of Deployment', 'Harm Domain', 'AI Harm Level',
    'Intentional Harm', 'Rights Violation', 'Risk Domain',
    'Risk Subdomain', 'deployer', 'developer', 'Location Region',
    'Lives Lost', 'Injuries', 'report_count'
]
clean = df[keep].copy()

clean['year'] = pd.to_numeric(clean['year'], errors='coerce')
clean['Incident Year'] = pd.to_numeric(clean['Incident Year'], errors='coerce')
clean['Chart Year'] = clean['year'].fillna(clean['Incident Year']).astype('Int64')

def first_sector(val):
    if pd.isna(val):
        return 'Not specified'
    try:
        parsed = ast.literal_eval(val)
        if isinstance(parsed, list) and len(parsed) > 0:
            return parsed[0]
    except (ValueError, SyntaxError):
        pass
    return str(val).strip('[]"\'')

clean['Primary Sector'] = clean['Sector of Deployment'].apply(first_sector)

clean.to_csv('aiid_dashboard_source.csv', index=False)
print(clean.shape)
print('nulls in Chart Year:', clean['Chart Year'].isna().sum())
print(clean['Chart Year'].value_counts().sort_index().tail(10))
