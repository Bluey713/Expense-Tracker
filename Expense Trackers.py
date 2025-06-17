#Project suggested by Grok to track expenses
#Create a program that tracks daily expenses, categorizes them, and provides
#basic insights(total spent, unique categories, or expenses above a threshold)

#lists: store expense entries
#Dictionaries: map expenses to categories and amounts
#set: find unique categories
#requirements:
#allow user to input expenses
#store expenses in a dictionary with categories as keys and lists of amounts as values
#provide options to view total spent accross all categories, list unique categories, show expenses above a user specified amount

expenses = {"Food": {"Groceries": 0, "Fast Food": 0},
            "Gas": 0,
            "Phone/Internet": 0,
            "Utilities": {"Gas":0, "Electricity": 0, "Water": 0},

             }
def user_choice():
    #This is the starting point of the whole loop. Will take user input to see if the want to add or view
    choice = int(input("What would you like to do? 1.Enter Expense 2.View Totals: "))
    if choice == 1:
        enter_expenses()
    else:
        view_totals()

def enter_expenses():
    #This will be the main function to take the user input and properly allocate expenses
    expense_entry = int(input("Which category would you like to enter? 1.Food 2.Gas 3.Phone/Internet 4.Utilities: "))
    if expense_entry == 1:
        sub_category = input("This category has selectable sub-categories. Which")
        print(f"This category has sub-categories")
        amount = float(input("Enter the "))
        #Need to figure out how to give a value to a nested dictionary
    elif expense_entry == 2:
        pass
    elif expense_entry == 3:
        pass
    elif expense_entry == 4:
        pass

def view_totals():
    #Will use this to ask user which expense account or sub account the want to view
    user_view = input("Which total would you like to view: ")
    pass

def total_threshold():
    #Will use to take user input and search for expense totals exceeding or equal to dependin on
    #user input
    pass