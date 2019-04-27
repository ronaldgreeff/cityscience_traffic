# cityscience_traffic

A (Django) RESTful API providing traffic counts for Devon, South West.


## BUILD
* Python==3.7
* Django==2.2
* djangorestframework==3.9.2


## SETTING UP LOCALLY
1. Set up your Postgres database
2. Edit environment details env.ps1 / env.sh to reflect your database settings
3. Start the virtualenv with:

  * ### Bash
      * $ python -m venv venv
      * $ $ source venv/scripts/activate
      * $ source ./env.sh

  * ### PowerShell
      * $ python -m venv venv
      * $ venv\scripts\activate
      * $ .\env.ps1

4. $ pip install -r requirements.txt
5. $ django manage.py makemigrations
6. $ django manage.py migrate
7. Import Devon.csv data into database by running 'python import_csv.py'
8. Run 'python manage.py runserver' and check that the data succesfully imported by visiting http://127.0.0.1:8000


## DEMO
https://citysci-traffic.azurewebsites.net


## HOW TO USE

Manual:
 * Navigate to API root (127.0.0.1:8000, or the demo link above).
 * Select the link http://citysci-traffic.azurewebsites.net/records/
 * Click "Filters" in the top right
 * Enter the details you would like to filter by

Programatic:
 * Generate a url with the necessary query paramaters. For example:
   http://citysci-traffic.azurewebsites.net/records/?year=2000&estimation_method=Counted&road=A381

   Would filter records by:
    * Year: 2000
    * Estimation Method: Counted
    * Road: A381