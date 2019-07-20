# ConvertMaster
Convert Master is a free online file converter which can be used for the following conversion:- XML to JSON,XML to CSV,JSON to XML ,JSON to CSV,CSV to JSON,CSV to JSON. Convert Master can also be used for downloading the converted file and also to preview the converted file on the go. Registered Users can also view and download all of their converted files after a secure login. This project was developed under __CESS Summer of Code 2.0__ by Team D'Coders. @mention:[Harmandeep Singh](https://github.com/SinghHrmn) along with @mention:[Kriti Rikhi ](https://github.com/kritirikhi)build the project from scratch.
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
Documentation will be released soon
