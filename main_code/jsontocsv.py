import pandas as pd


data_df = pd.read_json('parsed.json', orient='records')
data_df.to_csv('output.csv',index=False)