from django.urls import path
from .views import *

urlpatterns = [
    
    path('', index, name='landing_page'),
    # path('convert/xml-to-json', xmlToJson),
    # path('convert/xml-to-csv', xmlToCsv ),
    # path('convert/csv-to-json', csvToJson),
    # path('convert/csv-to-xml', csvToXml),
    # path('convert/json-to-csv', jsonToCsv),
    # path('convert/json-to-xml', jsonToXml),

]
