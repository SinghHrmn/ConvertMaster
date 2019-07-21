import xmltodict
import pprint
import json

with open('myData.xml') as fd:
    doc = xmltodict.parse(fd.read())

jsonFile = open('json_from_xml.json', 'w')
out = json.dumps(doc, indent=" ")
jsonFile.write(out)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(json.dumps(doc))
