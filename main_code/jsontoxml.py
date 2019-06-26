
import xmltodict
import json

data = open('json_from_xml.json', 'r').read()
data = json.loads(data)

# import xmltodict

# student = {
#   "data" : {
#     "name" : "Shubham",
#     "marks" : {
#       "math" : 92,student
#       "english" : 99
#     },
#     "id" : "s387hs3"
#   }
# }
# data = {
#  "csv_data": {
#   "row": [
#    {
#     "name": "Harmandeep Singh",
#     "class": "B.Tech CSE",
#     "rollno": "2017CSA1080"
#    },
#    {
#     "name": "Gursharandeep Singh",
#     "class": "B.Tech CSE",
#     "rollno": "2017CSA1076"
#    },
#    {
#     "name": "Harmandeep Singh",
#     "class": "B.Tech CSE",
#     "rollno": "2017CSA1078"
#    },
#    {
#     "name": "Kriti Rikhi",
#     "class": "B.Tech CSE",
#     "rollno": "2017CSA1110"
#    }
#   ]
#  }
# }
out = open('xml_from_json.xml','w')

out.write(xmltodict.unparse(data, pretty=True))


# data = json.dumps(data)
# print(len(data))# 
# print(data)

# print(xmltodict.unparse(data))
