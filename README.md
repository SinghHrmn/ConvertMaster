# ConvertMaster
Convert Master is a free online file converter which can be used for the following conversions:- 
* __XML to JSON__
* __XML to CSV__
* __JSON to XML__ 
* __JSON to CSV__
* __CSV to JSON__
* __CSV to JSON__ 
Convert Master can also be used for downloading the converted file and also to preview the converted file on the go. Registered Users can also view and download all of their converted files after a secure login. This project was developed under __CESS Summer of Code 2.0__ by Team D'Coders. @mention:[Harmandeep Singh](https://github.com/SinghHrmn) along with @mention:[Kriti Rikhi ](https://github.com/kritirikhi)build the project from scratch.
# Installation Guide
1.  Setup a virtual enviornment inside directory __ConvertMaster__. Though it is not neccessary but recommended.
    ```bash
    mastervulcan@MasterVulcan:~/ConvertMaster$ pipenv --python 'path/to/python'
    ```
2.  After creating the virtual enviornment start a shell inside the Virtualenv.
    ```bash
    mastervulcan@MasterVulcan:~/ConvertMaster$ pipenv shell
    ```
3.  Install all the dependancies for the project from __requirements.txt__.
    ```bash
    (convertmaster) mastervulcan@MasterVulcan:~/ConvertMaster$ pip install -r 'requirements.txt'
    ```
4.  After all the dependencies are installed, we will start a __local django server__. 
    * First of all we will move to the __ConvertMaster/src__ the directory where __manage.py__ is located.
    ```bash
    (convertmaster) mastervulcan@MasterVulcan:~/ConvertMaster$ cd src 
    (convertmaster) mastervulcan@MasterVulcan:~/ConvertMaster/src$
    ```
    * Then we will start making migrations for all the apps.
    ```bash
    (convertmaster) mastervulcan@MasterVulcan:~/ConvertMaster/src$ python manage.py makemigrations
    (convertmaster) mastervulcan@MasterVulcan:~/ConvertMaster/src$ python manage.py migrate
    ```
    * Now its time to create a __SuperUser__ to fully access the admin area. After running the following command fill the details
      and you are ready to go.
    ```bash
    (convertmaster) mastervulcan@MasterVulcan:~/ConvertMaster/src$ python manage.py createsuperuser
    ```
    * Now to run local server run the following command.
    ```bash
    (convertmaster) mastervulcan@MasterVulcan:~/ConvertMaster/src$ python manage.py runserver
    ```
5.  After the local server starts jump to your browser and open the following __url__ and enjoy the App.
    ```
    https://127.0.0.1:8000/
    ```
  
# Documentation
## XML to CSV
For Converting XML to CSV we will provide XML data which must include the <csv_data></csv_data> as firsrt root and each data should be included in row tag. The exaple code is given below
### XML CODE
```xml
    <?xml version="1.0"?>
    <csv_data>
    <row>
        <name>Harmandeep Singh</name>
        <class>B.Tech CSE</class>
        <rollno>2017CSA1080</rollno>
    </row>
    <row>
        <name>Gursharandeep Singh</name>
        <class>B.Tech CSE</class>
        <rollno>2017CSA1076</rollno>
    </row>
    <row>
        <name>Harmandeep Singh</name>
        <class>B.Tech CSE</class>
        <rollno>2017CSA1078</rollno>
    </row>
    <row>
        <name>Kriti Rikhi</name>
        <class>B.Tech CSE</class>
        <rollno>2017CSA1110</rollno>
    </row>
    <row>
        <name>Karan Choudhary</name>
        <class>B. Tech CSE</class>
        <rollno>2017CSA1102</rollno>
    </row>
    </csv_data>
```
### CSV CODE
```csv
class,name,rollno
B.Tech CSE,Harmandeep Singh,2017CSA1080
B.Tech CSE,Gursharandeep Singh,2017CSA1076
B.Tech CSE,Harmandeep Singh,2017CSA1078
B.Tech CSE,Kriti Rikhi,2017CSA1110
B.Tech CSE,Karan Choudhary,2017CSA1102
```
## XML to JSON
For Converting XML to JSON we will provide XML data which can be of any size. Here is some example code. 
### XML CODE
```xml
    <?xml version="1.0"?>
    <csv_data>
    <row>
        <name>Harmandeep Singh</name>
        <class>B.Tech CSE</class>
        <rollno>2017CSA1080</rollno>
    </row>
    <row>
        <name>Gursharandeep Singh</name>
        <class>B.Tech CSE</class>
        <rollno>2017CSA1076</rollno>
    </row>
    <row>
        <name>Harmandeep Singh</name>
        <class>B.Tech CSE</class>
        <rollno>2017CSA1078</rollno>
    </row>
    <row>
        <name>Kriti Rikhi</name>
        <class>B.Tech CSE</class>
        <rollno>2017CSA1110</rollno>
    </row>
    </csv_data>
```
### JSON CODE
```json
{
 "csv_data": {
  "row": [
   {
    "name": "Harmandeep Singh",
    "class": "B.Tech CSE",
    "rollno": "2017CSA1080"
   },
   {
    "name": "Gursharandeep Singh",
    "class": "B.Tech CSE",
    "rollno": "2017CSA1076"
   },
   {
    "name": "Harmandeep Singh",
    "class": "B.Tech CSE",
    "rollno": "2017CSA1078"
   },
   {
    "name": "Kriti Rikhi",
    "class": "B.Tech CSE",
    "rollno": "2017CSA1110"
   }
  ]
 }
}
```
## JSON to CSV
For Converting JSON to CSV we will provide JSON data which must include "csv_data" and "row" and the actual CSV data must be in "row". Here is some example code. 
### JSON
```json
{
 "csv_data": {
  "row": [
   {
    "name": "Harmandeep Singh",
    "class": "B.Tech CSE",
    "rollno": "2017CSA1080"
   },
   {
    "name": "Gursharandeep Singh",
    "class": "B.Tech CSE",
    "rollno": "2017CSA1076"
   },
   {
    "name": "Harmandeep Singh",
    "class": "B.Tech CSE",
    "rollno": "2017CSA1078"
   },
   {
    "name": "Kriti Rikhi",
    "class": "B.Tech CSE",
    "rollno": "2017CSA1110"
   }
  ]
 }
}
```
### CSV
```csv
class,name,rollno
B.Tech CSE,Harmandeep Singh,2017CSA1080
B.Tech CSE,Gursharandeep Singh,2017CSA1076
B.Tech CSE,Harmandeep Singh,2017CSA1078
B.Tech CSE,Kriti Rikhi,2017CSA1110
```

## JSON to XML
For Converting JSON to XML we will provide JSON data which can be of any size. Here is some example code. 
### JSON
```json
{
 "csv_data": {
  "row": [
   {
    "name": "Harmandeep Singh",
    "class": "B.Tech CSE",
    "rollno": "2017CSA1080"
   },
   {
    "name": "Gursharandeep Singh",
    "class": "B.Tech CSE",
    "rollno": "2017CSA1076"
   },
   {
    "name": "Harmandeep Singh",
    "class": "B.Tech CSE",
    "rollno": "2017CSA1078"
   },
   {
    "name": "Kriti Rikhi",
    "class": "B.Tech CSE",
    "rollno": "2017CSA1110"
   }
  ]
 }
}
```
### XML CODE
```xml
<?xml version="1.0" encoding="utf-8"?>
<csv_data>
	<row>
		<name>Harmandeep Singh</name>
		<class>B.Tech CSE</class>
		<rollno>2017CSA1080</rollno>
	</row>
	<row>
		<name>Gursharandeep Singh</name>
		<class>B.Tech CSE</class>
		<rollno>2017CSA1076</rollno>
	</row>
	<row>
		<name>Harmandeep Singh</name>
		<class>B.Tech CSE</class>
		<rollno>2017CSA1078</rollno>
	</row>
	<row>
		<name>Kriti Rikhi</name>
		<class>B.Tech CSE</class>
		<rollno>2017CSA1110</rollno>
	</row>
</csv_data>
```
## CSV to XML
For Converting CSV to XML we will provide CSV data which can be of any size. Here is some example code. 
### CSV CODE
```csv
class,name,rollno
B.Tech CSE,Harmandeep Singh,2017CSA1080
B.Tech CSE,Gursharandeep Singh,2017CSA1076
B.Tech CSE,Harmandeep Singh,2017CSA1078
B.Tech CSE,Kriti Rikhi,2017CSA1110
```
### XML CODE
```xml
<?xml version="1.0" encoding="utf-8"?>
<csv_data>
	<row>
		<name>Harmandeep Singh</name>
		<class>B.Tech CSE</class>
		<rollno>2017CSA1080</rollno>
	</row>
	<row>
		<name>Gursharandeep Singh</name>
		<class>B.Tech CSE</class>
		<rollno>2017CSA1076</rollno>
	</row>
	<row>
		<name>Harmandeep Singh</name>
		<class>B.Tech CSE</class>
		<rollno>2017CSA1078</rollno>
	</row>
	<row>
		<name>Kriti Rikhi</name>
		<class>B.Tech CSE</class>
		<rollno>2017CSA1110</rollno>
	</row>
</csv_data>
```
## CSV to JSON
For Converting CSV to JSON we will provide CSV data which can be of any size. Here is some example code. 
### CSV CODE
```csv
class,name,rollno
B.Tech CSE,Harmandeep Singh,2017CSA1080
B.Tech CSE,Gursharandeep Singh,2017CSA1076
B.Tech CSE,Harmandeep Singh,2017CSA1078
B.Tech CSE,Kriti Rikhi,2017CSA1110
```
### JSON CODE
```json
{
 "csv_data": {
  "row": [
   {
    "name": "Harmandeep Singh",
    "class": "B.Tech CSE",
    "rollno": "2017CSA1080"
   },
   {
    "name": "Gursharandeep Singh",
    "class": "B.Tech CSE",
    "rollno": "2017CSA1076"
   },
   {
    "name": "Harmandeep Singh",
    "class": "B.Tech CSE",
    "rollno": "2017CSA1078"
   },
   {
    "name": "Kriti Rikhi",
    "class": "B.Tech CSE",
    "rollno": "2017CSA1110"
   }
  ]
 }
}
```
