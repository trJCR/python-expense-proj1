#This file will handle file input and output (r/w to CSV)
import csv
import os

data_folder = "data"
file_path = f"{data_folder}/expenses.csv"
expense_keys = ['date','category','name','amount','payment_method']

#functions in this file will be:

#function to make sure csv file exists
def ensure_folder():
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            new_csv = csv.DictWriter(f,expense_keys)
            new_csv.writeheader()

#load_expenses function will return list of all expenses read from csv
def load_expenses():
    """
    Reads expenses from expenses.csv
    Returns a list of dict, where each dict is an expense with its properties
    Example: [
        {'date': '2026-01-15', 'category': 'Food', 'name': 'Groceries', 'amount': 50.00, 'payment_method': 'Credit'},
        {'date': '2026-01-14', 'category': 'Gas', 'name': 'Shell', 'amount': 35.00, 'payment_method': 'Debit'}
    ]
    """
    #make sure file exists
    ensure_folder()

    #read from expenses.csv file
    try:
        with open(file_path, 'r') as f:
            full_expenses = csv.DictReader(f)
            expenses_list = list(full_expenses)

        if expenses_list == []:
            return []

        return expenses_list
    except FileNotFoundError:
        print(f"File not found")
        return []


#save_expenses(expense_list) will write the expenses into a csv file
def save_expenses(expense_list):

    #make sure file exists
    ensure_folder()

    #write expenses to the csv file
    try:
        with open(file_path, 'w') as f:
            expense_writer = csv.DictWriter(f,fieldnames=expense_keys)
            expense_writer.writeheader()
            
            for row in expense_list:
                expense_writer.writerow(row)
    except FileNotFoundError:
        print(f"File not found")
        return []
    