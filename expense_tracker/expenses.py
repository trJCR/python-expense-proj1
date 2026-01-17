import file_handler
from datetime import datetime
from collections import defaultdict
#This file will contain all functions related to calculating/sorting any expenses

#add_expense(amount,category,name,date,payment_method) -> makes a new expense record
def add_expense(amount,category,name,date,payment_method):

    #load csv into a variable (should be a list)
    loaded_csv = file_handler.load_expenses()

    #Check if amount can actually be converted to float/is a valid number
    try:
        if float(amount) <= 0:
            print(f"Amount must be positive")
            return False
    except ValueError:
        print(f"Amount is invalid")
        return False
    
    #Check if date is valid yyyy-mm-dd format
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print(f"Invalid date")
        return False

    #Check if something is empty or none
    if not amount or not category or not name or not date or not payment_method:
        print("One of the stats are empty")
        return False
    
    #create new expense dict with the parameters passed
    new_expense = {
        "amount": float(amount),
        "category": category,
        "name": name,
        "date": date,
        "payment_method": payment_method
    }

    #append new expense to end of list
    try:
        loaded_csv.append(new_expense)
        file_handler.save_expenses(loaded_csv)
        return True
    except (ValueError, FileNotFoundError, IOError) as e:
        print(f"Error adding expense: {e}")
        return False

#function to delete an expense after being given the name
#args: the name to be deleted
def delete_expense():
    all_expenses = file_handler.load_expenses()
    if not all_expenses:
        print(f"No expenses to delete.")
        return False
    
    #loop through expenses and assign an ID to it
    for index, expense in enumerate(all_expenses,1):
        print(f"{index}.{expense['date']:<12} {expense['category']:<15} {expense['name']:<20} ${float(expense['amount']):<11.2f} {expense['payment_method']:<15}")

    #ask user which to delete
    del_choice = input("Enter Index # of the expense to delete: ")

    try:
        #check choice
        del_id = int(del_choice)

        if del_id < 1 or del_id > len(all_expenses):
            print("Invalid choice.")
            return False
    except ValueError:
        print("Enter a valid number")
        return False
    
    deleted = all_expenses.pop(del_id - 1)
    file_handler.save_expenses(all_expenses)

    print(f"Deleted:  {deleted['name']} - ${deleted['amount']}")
    return True
        


#get_all_expenses() -> returns all expenses
#no args, returns a list of all expenses from csv
def get_all_expenses():
    read_expenses = file_handler.load_expenses()
    return read_expenses

#sort_by_category(expenses) -> sorts expenses by their category
#args: expenses (list of dicts)
#returns: a dict where keys are categories and values are lists of expenses
def sort_by_category(expenses):
    #defaultdict with list as the factory
    category_list = defaultdict(list)

    #loop through each expense
    for expense in expenses:
        #missing keys are defaulted to an empty list
        #existing keys are automatically appended to the category
        category_list[expense['category']].append(expense)
    return dict(sorted(category_list.items())) #convert back to regular dict

        


#sort_by_amount(expenses, order='high_to'low') -> sorts by price high2low
#args: expenses (list), order (str)
#returns: sorted list of expenses by amount
def sort_by_amount(expenses, order='high_to_low'):
    #default order is high to low which will make reverse = true
    #if order passed is low_to_high, then order will be false and reverse will be false
    #reverse being false will lead to ascending order (low to high)
    reverse =(order == 'high_to_low')
    return sorted(expenses, key=lambda expense: float(expense['amount']),reverse=reverse)

#sort_by_amount(expenses, order='low_to_high') -> sorts by price low2high

#sort_alphabetically(expenses) -> sorts by expense name in alphabetical order
#takes expense (a list), returns a list sorted a-z
#sorted() because .sort() modifies the original - want to keep original the same for other functions
def sort_alphabetically(expenses):
    return sorted(expenses, key=lambda expense: expense['name'].lower())

def export_to_json():
    import json

    all_expenses = file_handler.load_expenses()

    if not all_expenses:
        print("No expenses to report")
        return False
    filename = input("Enter filename (without .json): ")
    full_filename = f"data/{filename}.json"

    try:
        with open(full_filename, 'w') as f:
            json.dump(all_expenses, f, indent=2)
        
        print(f"Exported {len(all_expenses)} expenses to {full_filename}")

    except Exception as e:
        print(f"Error reporting: {e}")
        return False
