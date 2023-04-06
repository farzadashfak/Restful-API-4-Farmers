from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from datetime import datetime
from mongoengine import connect
from models import Income, Expense
from database import get_all_income, get_all_expenses

app = Flask(__name__)
api = Api(app)

connect('farmers_financial_management', host='localhost', port=27017)

@app.route('/')
def home():
    return 'Welcome to the financial management system for farmers!'

@app.route('/income', methods=['GET', 'POST'])
def income():
    if request.method == 'GET':
        income = get_all_income()
        return jsonify(income)
    elif request.method == 'POST':
        amount = request.json['amount']
        description = request.json['description']
        date = request.json['date']
        add_income(amount, description, date)
        return jsonify({"message": "Income added successfully!"})

@app.route('/expenses', methods=['GET', 'POST'])
def expenses():
    if request.method == 'GET':
        expenses = get_all_expenses()
        return jsonify(expenses)
    elif request.method == 'POST':
        amount = request.json['amount']
        description = request.json['description']
        date = request.json['date']
        add_expense(amount, description, date)
        return jsonify({"message": "Expense added successfully!"})
        
@app.route('/income-statement', methods=['GET'])
def income_statement():
    income = get_all_income()
    total_income = sum(i.amount for i in income)
    expenses = get_all_expenses()
    total_expenses = sum(e.amount for e in expenses)
    net_income = total_income - total_expenses
    return jsonify({
        "total_income": total_income,
        "total_expenses": total_expenses,
        "net_income": net_income
    })
    
@app.route('/balance-sheet', methods=['GET'])
def balance_sheet():
    assets = get_all_income()
    total_assets = sum(a.amount for a in assets)
    liabilities = get_all_expenses()
    total_liabilities = sum(l.amount for l in liabilities)
    equity = total_assets - total_liabilities
    return jsonify({
        "total_assets": total_assets,
        "total_liabilities": total_liabilities,
        "equity": equity
    })

if __name__ == '__main__':
    app.run(debug=True)
