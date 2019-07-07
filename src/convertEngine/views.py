from django.shortcuts import render
from django.contrib.auth.decorators import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def xmlToJson(request):
    return render(request,'convertEngine/xml_to_json.html')

def xmlToCsv(request):
    return render(request,'convertEngine/xml_to_csv.html')

def csvToJson(request):
    return render(request,'convertEngine/csv_to_json.html')

def csvToXml(request):
    return render(request,'convertEngine/csv_to_xml.html')

def jsonToCsv(request):
    return render(request,'convertEngine/json_to_csv.html')

def jsonToXml(request):
    return render(request,'convertEngine/json_to_xml.html')

def documentation(request):
    return render(request, 'convertEngine/doc.html')

@login_required
def myconversions(request):
    return render(request,'convertEngine/myconversions.html')
