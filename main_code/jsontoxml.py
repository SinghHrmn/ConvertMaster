
import xmltodict
import json

data = open('json_from_xml.json', 'r').readlines()
data = json.dumps(data)
print(data)

# print(xmltodict.unparse(data))
