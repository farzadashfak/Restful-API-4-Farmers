from flask import Flask, request
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort
from flask_restful_swagger import swagger
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
api = swagger.docs(Api(app), apiVersion='0.1', api_spec_url='/docs')

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['financial_management']

# Define data models
income_fields = {
    'id': fields.String,
    'date': fields.DateTime(dt_format='iso8601'),
    'description': fields.String,
    'amount': fields.Float
}

expense_fields = {
    'id': fields.String,
    'date': fields.DateTime(dt_format='iso8601'),
    'description': fields.String,
    'amount': fields.Float
}

balance_fields = {
    'income_total': fields.Float,
    'expense_total': fields.Float,
    'balance': fields.Float
}

income_parser = reqparse.RequestParser(bundle_errors=True)
income_parser.add_argument('date', type=str, required=True, help='Date of income (YYYY-MM-DD)')
income_parser.add_argument('description', type=str, required=True, help='Description of income')
income_parser.add_argument('amount', type=float, required=True, help='Amount of income')

expense_parser = reqparse.RequestParser(bundle_errors=True)
expense_parser.add_argument('date', type=str, required=True, help='Date of expense (YYYY-MM-DD)')
expense_parser.add_argument('description', type=str, required=True, help='Description of expense')
expense_parser.add_argument('amount', type=float, required=True, help='Amount of expense')

# Define API resources
class IncomeListResource(Resource):
    @swagger.operation(
        notes='Retrieve a list of income records',
        responseClass=list,
        nickname='get'
    )
    def get(self):
        income_records = list(db.income.find())
        return income_records

    @swagger.operation(
        notes='Add a new income record',
        responseClass=income_fields,
        nickname='post',
        parameters=[
            {
                'name': 'income',
                'description': 'Income data',
                'required': True,
                'allowMultiple': False,
                'dataType': income_parser,
                'paramType': 'body'
            }
        ]
    )
    @marshal_with(income_fields)
    def post(self):
        args = income_parser.parse_args()
        date = datetime.strptime(args['date'], '%Y-%m-%d')
        income_data = {
            'date': date,
            'description': args['description'],
            'amount': args['amount']
        }
        result = db.income.insert_one(income_data)
        income_data['id'] = str(result.inserted_id)
        return income_data

class ExpenseListResource(Resource):
    @swagger.operation(
        notes='Retrieve a list of expense records',
        responseClass=list,
        nickname='get'
    )
    def get(self):
        expense_records = list(db.expense.find())
        return expense_records

    @swagger.operation(
        notes='Add a new expense record',
        responseClass=expense_fields,
        nickname='post',
        parameters=[
            {
                'name': 'expense',
                'description': 'Expense data',
                'required': True,
                'allowMultiple': False,
                'dataType': expense_parser,
                'paramType': 'body'
            }
        ]
    )
