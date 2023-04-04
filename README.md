# Restful-API-4-Farmers

# Financial Management System API #

This is a basic RESTful API for a financial management system for farmers using Python. The API allows farmers to interact with the system by providing input data (e.g., income, expenses, etc.) and receiving financial statements, including income statements and balance sheets as output.

## Technologies Used ##

Python 3.9
Flask 2.0.2
Flask-RESTful 0.3.9
Flask-RESTful-Swagger 0.21.0
MongoDB 4.4.4

## Getting Started ##

1. Clone this repository to your local machine.
2. Install Python 3.9 or later.
3. Install the required dependencies using pip install -r requirements.txt.
4. Start the application using python app.py.
5. The API will be accessible at http://localhost:5000/.

## API Endpoints ##

### /income ###
**GET:** Retrieve a list of income records
**POST**: Add a new income record
### /expense ###
**GET:** Retrieve a list of expense records
**POST:** Add a new expense record
### /balance ###
**GET:** Retrieve an income statement and balance sheet for the current year

