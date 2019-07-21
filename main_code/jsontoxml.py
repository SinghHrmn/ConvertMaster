
import xmltodict
import json

data = open('json_from_xml.json', 'r').read()
data = json.loads(data)

out = open('xml_from_json.xml','w')

out.write(xmltodict.unparse(data, pretty=True))
