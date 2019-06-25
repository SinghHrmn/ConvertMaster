import csv  
import json  
    
# Open the CSV  
csvfile = open( 'test_file_Csv.csv', 'r' )  
reader = csv.DictReader(csvfile)   
out = json.dumps( [ row for row in reader ],indent=" " )
jsonfile = open( 'parsed.json', 'w')  
jsonfile.write(out)