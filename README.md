#This is a  data analysis application using Python and Django

The source of the open-data data used in this project is https://climate.nasa.gov/vital-signs/global-temperature/

#Follow these steps to start the program and access it


Step 1)To enter the virtual environment, you need to enter the venv folder under the project in the terminal
        cd venv
        .\Scripts\activate

Step 2）Perform a migration operation to create the table
       python manage.py makemigrations
       python manage.py migrate

Step 3)Execute the parse.py file for data reading, and the data will be stored in the database table after execution
       python manage.py parse

Step 4)Start the server
       python manage.py runserver

Step 5)Visit the server, enter 'http://127.0.0.1:8000/parse_work/index' in the address bar of the browser to display the main page of the data, click the year of each row of data to jump to the page, and the new page will display the year’s Relevant data on CO2 for each month
