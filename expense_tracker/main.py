import expenses
import file_handler
#Main python file for running loops calling functions from expenses.py

#function will display table in a formatted table
#args taken: expenses as a list of dicts
def display_expenses_table(expenses):
    #check if expenses even exist
    if not expenses:
        print("No expenses to display.\n")
        return
    
    #print table w header and width specifiers
    print("\n" + "="*100) #print header
    print(f"{'Date':<12} {'Category':<15} {'Name':<20} {'Amount':<12} {'Payment Method':<15}")
    print("="*100)

    #print each expense
    for expense in expenses:
        print(f"{expense['date']:<12} {expense['category']:<15} {expense['name']:<20} ${float(expense['amount']):<11.2f} {expense['payment_method']:<15}")
    print("\n" + "="*100)

#function will display menu and the choices
def display_menu():
    print("\n" + "="*50)
    print("       EXPENSE TRACKER MENU")
    print("="*50)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Sort by Category")
    print("4. Sort by Amount")
    print("5. Sort Alphabetically")
    print("6. Delete an Expense")
    print("7. Export to json file")
    print("8. Exit program")
    print("="*50)

#function will be called when adding an expense for user to manually input expense data
def input_expenses():
    print("\n--- ADD NEW EXPENSE ---")

    #prompt each field
    date = input("Enter date in (YYYY-MM-DD) Format: ")
    category = input("Enter category (Food, Gas, Clothes, etc.): ")
    name = input("Enter name of expense: ")
    amount = input("Enter amount: $")
    payment_method = input("Enter payment method (Cash, Credit, Debit): ")

    success = expenses.add_expense(amount,category,name,date,payment_method)

    if success:
        print("Expense was added successfully")
    else:
        print("Failed to add expense, please check inputs. \n")

def display_expenses_by_category(category_dict):
    """
    Display expenses grouped by category
    
    Args:
        category_dict (dict): Dictionary where keys are categories and values are lists of expenses
    """
    if not category_dict:
        print("No expenses to display.\n")
        return
    
    for category, expenses_list in category_dict.items():
        print(f"\n{'='*100}")
        print(f"Category: {category.upper()}")
        print(f"{'='*100}")
        
        # Display expenses in this category
        print(f"{'Date':<12} {'Name':<20} {'Amount':<12} {'Payment Method':<15}")
        print("-"*100)
        
        for expense in expenses_list:
            print(f"{expense['date']:<12} {expense['name']:<20} ${float(expense['amount']):<11.2f} {expense['payment_method']:<15}")
        
        # Show category total
        total = sum(float(expense['amount']) for expense in expenses_list)
        print(f"{'Category Total:':<32} ${total:.2f}\n")


#main function
def main():
    #Main loop, loop through
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == '1': #Add an expense
            input_expenses()

        elif choice == '2': #View all expenses
            all_expenses = expenses.get_all_expenses()
            if not all_expenses:
                print("No expenses to sort.\n")
            else:
                display_expenses_table(all_expenses)
        
        elif choice == '3': #Sort by category
            all_expenses = expenses.get_all_expenses()
            if not all_expenses:
                print("No expenses to sort.\n")
            else:
                cat_sort_expenses = expenses.sort_by_category(all_expenses)
                display_expenses_by_category(cat_sort_expenses)

        elif choice == '4': #sort by amount
            all_expenses = expenses.get_all_expenses()
            if not all_expenses:
                print("No expenses to sort.\n")
            else:
                order_choice = input("In what order? Enter 1 for High to Low, 2 for Low to High: ")
                if order_choice == "1":
                    display_expenses_table(expenses.sort_by_amount(all_expenses,'high_to_low'))
                elif order_choice == "2":
                    display_expenses_table(expenses.sort_by_amount(all_expenses,'low_to_high'))
                else:
                    print("Invalid choice.")
        
        elif choice == "5":
            all_expenses = expenses.get_all_expenses()
            if not all_expenses:
                print("No expenses to sort.\n")
            else:
                sorted_alpha = expenses.sort_alphabetically(all_expenses)
                display_expenses_table(sorted_alpha)

        elif choice == "6":
            all_expenses = expenses.get_all_expenses()
            if not all_expenses:
                print("No expenses to sort.\n")
            else:
                expenses.delete_expense()

        elif choice == "7":
            expenses.export_to_json()

        elif choice == "8":
            break

        else:
            print(f"Invalid choice.")

if __name__ == "__main__":
    main()