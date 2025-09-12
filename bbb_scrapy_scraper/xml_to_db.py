import pandas as pd
import dbload

# this script will convert xml to dataframe then insert in the db

namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

df = pd.read_xml("sitemap1.xml", xpath="//ns:url",namespaces=namespaces)

df = df[['loc']]
df['loc'] = df['loc'].astype(str)
df['loc'] = df['loc'].str.strip().str.lower()
df = df.drop_duplicates(subset='loc',keep='first')

df['sitemap_no'] = 1

df.rename(columns={'loc':'url'},inplace=True)

df.to_sql('sitemaps',con=dbload.sqlengine(),if_exists='append',index=False)
