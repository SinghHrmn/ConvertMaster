import xmltodict
import json
import pandas as pd

with open('myData.xml') as fd:
    doc = xmltodict.parse(fd.read())
out = json.dumps(doc)
data = json.loads(out)

x = data['csv_data']['row']
data_df = pd.DataFrame(x)
data_df.to_csv('output2.csv',index=False)

