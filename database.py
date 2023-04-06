from pymongo import MongoClient
from models import Income, Expense

client = MongoClient("mongodb://localhost:27017/")
db = client["financial_db"]

def add_income(amount, description, date):
    income = Income(amount=amount, description=description, date=date)
    income.save()
    
def add_expense(amount, description, date):
    expense = Expense(amount=amount, description=description, date=date)
    expense.save()

def get_all_income():
    return Income.objects()

def get_all_expenses():
    return Expense.objects()

