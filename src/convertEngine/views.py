from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import *
import os
from datetime import datetime
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
        # Retrieveing the post data
        xml_data = request.POST['xml']
        
        #creating the file name based on time
        filename = ""
        name = datetime.now()
        filename += str(name.year)+str(name.month)+str(name.day)+str(name.hour)+str(name.minute)+str(name.second)+str(name.microsecond)

        # Writing the post data to the file
        input_file_name = filename + '.xml'
        saved_file = open(os.path.join(settings.MEDIA_ROOT, input_file_name), 'w')
        saved_file.write(xml_data)
        saved_file.close()

        output_file_name = filename + '.json'
        with open('/media/'+ input_file_name) as fd:
            doc = xmltodict.parse(fd.read())

        jsonFile = open(os.path.join(settings.MEDIA_ROOT, output_file_name), 'w')
        out = json.dumps(doc, indent=" ")
        jsonFile.write(out)
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(json.dumps(doc))
        return HttpResponse('<p>'+str(pp)+'</p>')
        
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
        # Retrieveing the post data
        csv_data = request.POST['csv']
        
        #creating the file name based on time
        filename = ""
        name = datetime.now()
        filename += str(name.year)+str(name.month)+str(name.day)+str(name.hour)+str(name.minute)+str(name.second)+str(name.microsecond)

        # Writing the post data to the file
        input_file_name = filename + '.csv'
        saved_file = open(os.path.join(settings.MEDIA_ROOT, input_file_name), 'w')
        saved_file.write(csv_data)
        saved_file.close()

        # Converting the csv file to the json format
        output_file_name = filename + '.json' 
        csvfile = open(os.path.join(settings.MEDIA_ROOT, input_file_name), 'r' )  
        reader = csv.DictReader(csvfile)   
        out = json.dumps( [ row for row in reader ],indent=" " )
        jsonfile = open(os.path.join(settings.MEDIA_ROOT, output_file_name), 'w')  
        jsonfile.write(out)
        jsonfile.close()
        return HttpResponse('<p>'+str(out)+'</p>')
    else:
        return render(request,'convertEngine/csv_to_json.html')

# -------------------------------CSV-TO-XML----------------------------------------------
def csvToXml(request):
    if request.method == 'POST':
        # Retrieveing the post data
        csv_data = request.POST['csv']
        # print('csv data recieved')
        #creating the file name based on time
        filename = ""
        name = datetime.now()
        filename += str(name.year)+str(name.month)+str(name.day)+str(name.hour)+str(name.minute)+str(name.second)+str(name.microsecond)
        # print('filename created')
        # print(filename)
        # Writing the post data to the file
        input_file_name = filename + '.csv'
        saved_file = open(os.path.join(settings.MEDIA_ROOT, input_file_name), 'w')
        saved_file.write(csv_data)
        saved_file.close()
        print(input_file_name)
        
        output_file_name = filename + '.xml'
        
        
        # csvData = csv.reader(open('/media/'+ input_file_name))
        csvData = open('/media/'+input_file_name)
        csvData = csv.reader(csvData)
        xmlData = open(os.path.join(settings.MEDIA_ROOT, output_file_name), 'w')
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
        return HttpResponse('Conversion Done')
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
