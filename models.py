from mongoengine import connect
connect('farmers_financial_management', host='localhost', port=27017)

from mongoengine import Document, DecimalField, StringField, DateTimeField
class Income(Document):
    amount = DecimalField(precision=2, required=True)
    description = StringField(max_length=100, required=True)
    date = DateTimeField(required=True)

class Expense(Document):
    amount = DecimalField(precision=2, required=True)
    description = StringField(max_length=100, required=True)
    date = DateTimeField(required=True)