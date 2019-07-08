from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import *
import os
from django.conf import settings
import pandas as pd
import csv
import json  
import xmltodict
import pprint
import dicttoxml


# =========================renders the landing page======================================
def index(request):
    return render(request,'index.html')

# # =======================CONVERSION CODE STARTS=========================================
# -------------------------------XML-TO-JSON----------------------------------------------
def xmlToJson(request):
    if request.method == 'POST':
        with open('myData.xml') as fd:
            doc = xmltodict.parse(fd.read())

        jsonFile = open('json_from_xml.json', 'w')
        out = json.dumps(doc, indent=" ")
        jsonFile.write(out)
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(json.dumps(doc))
        
    else:
        return render(request,'convertEngine/xml_to_json.html')

# -------------------------------XML-TO-CSV----------------------------------------------
def xmlToCsv(request):
    if request.method == 'POST':
        with open('myData.xml') as fd:
            doc = xmltodict.parse(fd.read())
        out = json.dumps(doc)
        data = json.loads(out)

        x = data['csv_data']['row']
        data_df = pd.DataFrame(x)
        data_df.to_csv('output2.csv',index=False)
    else:
        return render(request,'convertEngine/xml_to_csv.html')

# -------------------------------CSV-TO-JSON----------------------------------------------
def csvToJson(request):
    if request.method == 'POST':
    
        csvfile = open( 'test_file_Csv.csv', 'r' )  
        reader = csv.DictReader(csvfile)   
        out = json.dumps( [ row for row in reader ],indent=" " )
        jsonfile = open( 'parsed.json', 'w')  
        jsonfile.write(out)
    else:
        return render(request,'convertEngine/csv_to_json.html')

# -------------------------------CSV-TO-XML----------------------------------------------
def csvToXml(request):
    if request.method == 'POST':
    
        csvFile = 'test_file_Csv.csv'
        xmlFile = 'myData.xml'

        csvData = csv.reader(open(csvFile))
        xmlData = open(xmlFile, 'w')
        xmlData.write('<?xml version="1.0"?>' + "\n")
        # there must be only one top-level tag
        xmlData.write('<csv_data>' + "\n")

        rowNum = 0
        for row in csvData:
            if rowNum == 0:
                tags = row
                # replace spaces w/ underscores in tag names
                for i in range(len(tags)):
                    tags[i] = tags[i].replace(' ', '_')
            else: 
                xmlData.write('<row>' + "\n")
                for i in range(len(tags)):
                    xmlData.write('    ' + '<' + tags[i] + '>' + row[i] + '</' + tags[i] + '>' + "\n")
                xmlData.write('</row>' + "\n")
                    
            rowNum +=1

        xmlData.write('</csv_data>' + "\n")
        xmlData.close()
    else:
        return render(request,'convertEngine/csv_to_xml.html')

# -------------------------------JSON-TO-CSV----------------------------------------------
def jsonToCsv(request):
    if request.method == 'POST':
    
        data_df = pd.read_json('parsed.json', orient='records')
        data_df.to_csv('output.csv',index=False)
    else:
        return render(request,'convertEngine/json_to_csv.html')

# -------------------------------JSON-TO-XML----------------------------------------------
def jsonToXml(request):
    if request.method == 'POST':
    
        data = open('json_from_xml.json', 'r').read()
        data = json.loads(data)

        out = open('xml_from_json.xml','w')

        out.write(xmltodict.unparse(data, pretty=True))
    else:
        return render(request,'convertEngine/json_to_xml.html')

# # ====================CONVERSION_CODE_ENDS================================================
def documentation(request):
    return render(request, 'convertEngine/doc.html')

# ====================shows previous convertions for logined users==========================
@login_required
def myconversions(request):
    return render(request,'convertEngine/myconversions.html')

# ===========================TEST FUNC===============================
def test(request):
    x = "Hello world"
    # user = request.session['User']
    filename = '6-06-2019'
    y = open(os.path.join(settings.MEDIA_ROOT, 'file.txt'), 'w')
    y.write(x)
    y.close()
    return HttpResponse('test done')
