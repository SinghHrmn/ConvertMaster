from django.urls import path
from .views import *

urlpatterns = [
    
    path('', index, name='landing_page'),
    path('test/', test, name='landing_page'),
    path('convert/xml-to-json', xmlToJson, name='xml-json'),
    path('convert/xml-to-csv', xmlToCsv, name='xml-csv'),
    path('convert/csv-to-json', csvToJson, name='csv-json'),
    path('convert/csv-to-xml', csvToXml, name='csv-xml'),
    path('convert/json-to-csv', jsonToCsv, name='json-csv'),
    path('convert/json-to-xml', jsonToXml, name='json-xml'),
    path('convert/Documentation', documentation, name='Doc'),
    path('convert/myconversions', myconversions, name='myconversions'),




]
