#Project suggested by Grok to track expenses
#Create a program that tracks daily expenses, categorizes them, and provides
#basic insights(total spent, unique categories, or expenses above a threshold)

#lists: store expense entries
#Dictionaries: map expenses to categories and amounts - This part is done but user cant add new accounts
#set: find unique categories
#requirements:
#allow user to input expenses - This part is done but limited to existing expense accounts
#store expenses in a dictionary with categories as keys and lists of amounts as values
#provide options to view total spent accross all categories, list unique categories, show expenses above a user specified amount

#Functions should only have one task, they should not be asking for input



#import sys
expense_list = ["Food", "Gas", "Insurance", "Property Tax", "Utilities"] #"Groceries", "Fast Food"
#Still need to thing about how to incorporate lists. So far im just using a giant dictionary


#Functions

def user_choice(): #Not used
    # This is the starting point of the whole loop. Will take user input to see if the want to add or view
    try:
        choice = int(input("What would you like to do? 1.Enter Expense 2.View Totals 3.Quit: "))
        if choice == 1:
            enter_expenses()
        elif choice == 2:
            view_totals()
        elif choice ==3:
            print("See you next time!")
            return False
    except:
        print("You didn't enter a valid response. Try again.")
        return True
#Decided to scrap this functions and just use the block of code inside the while loop instead. Had an issue break out of the loop this way


def enter_expenses(expense_entry, expenses_dict):
    #This will be the main function to take the user input and properly allocate expenses
    if expense_entry == "Food":
        for key in expenses_dict[expense_entry]:
            print(key)
        #Thinking of adding a loop to check if the key selected includes a value or if its type(dict) then to print out all keys
        sub_category = input("This category has the stated selectable sub-categories. Which do you want to access: ").strip().title()
        if sub_category == "Groceries":
            amount = float(input(f"Enter the amount of the expense for {sub_category} ")) #maybe switch these to f strings and include the key
            expenses_dict[expense_entry][sub_category] += amount
            print(f"The updated value of {sub_category} is: {expenses_dict[expense_entry][sub_category]}")
        elif sub_category == "Fast Food":
            amount = float(input(f"Enter the amount of the expense for {sub_category}: "))
            expenses_dict[expense_entry][sub_category] += amount
            print(f"The updated value of {sub_category} is: {expenses_dict[expense_entry][sub_category]}")

    elif expense_entry == "Gas":
        amount = float(input(f"Enter the amount of the expense for {expense_entry}: "))  # maybe switch these to f strings and include the key
        expenses_dict[expense_entry] += amount
        print(f"The updated value of {expense_entry} is: {expenses_dict[expense_entry]}")

    elif expense_entry == "Phone/Internet":
        amount = float(input(f"Enter the amount of the expense for {expense_entry}: "))  # maybe switch these to f strings and include the key
        expenses_dict[expense_entry] += amount
        print(f"The updated value of {expense_entry} is: {expenses_dict[expense_entry]}")

    elif expense_entry == "Utilities":
        for key in expenses_dict[expense_entry]:
            print(key)
        #Thinking of adding a loop to check if the key selected includes a value or if its type(dict) then to print out all keys
        sub_category = input("This category has the stated selectable sub-categories. Which do you want to access: ").strip().title()
        if sub_category == "Gas":
            amount = float(input(f"Enter the amount of the expense for {sub_category}: ")) #maybe switch these to f strings and include the key
            expenses_dict[expense_entry][sub_category] += amount
            print(f"The updated value of {sub_category} is: {expenses_dict[expense_entry][sub_category]}")
        if sub_category == "Electricity":
            amount = float(input(f"Enter the amount of the expense for {sub_category}: ")) #maybe switch these to f strings and include the key
            expenses_dict[expense_entry][sub_category] += amount
            print(f"The updated value of {sub_category} is: {expenses_dict[expense_entry][sub_category]}")
        if sub_category == "Water":
            amount = float(input(f"Enter the amount of the expense for {sub_category}: ")) #maybe switch these to f strings and include the key
            expenses_dict[expense_entry][sub_category] += amount
            print(f"The updated value of {sub_category} is: {expenses_dict[expense_entry][sub_category]}")

    return expense_entry

def continue_entering():
    pass
    #is this function required to keep the program running?
    #was thinking of having additional print statements asking to continue or print out stuff which would just call the previous functions


def view_totals(user_view):
    #Will use this to take user input on which expense account or sub account the want to view
    if user_view == "Food":
        for key in expenses_dict[user_view]:
            print(key)
        # Thinking of adding a loop to check if the key selected includes a value or if its type(dict) then to print out all keys
        sub_category = input("This category has the stated selectable sub-categories. Would you like 1.Total 2.Groceries 3.Fast Food?: ").strip().title()
        if sub_category == "Total":
            print(sum(expenses_dict[user_view].values()))   #Prints the sum of values in food
        elif sub_category == "Groceries":
            print(f"The current value of {sub_category} is: {expenses_dict[expense_entry][sub_category]}")
        elif sub_category == "Fast Food":
            print(f"The current value of {sub_category} is: {expenses_dict[expense_entry][sub_category]}")

    elif expense_entry == "Gas":
        print(f"The current value of {expense_entry} is: {expenses_dict[expense_entry]}")

    elif expense_entry == "Phone/Internet":
        print(f"The current value of {expense_entry} is: {expenses_dict[expense_entry]}")

    elif expense_entry == "Utilities":
        for key in expenses_dict[expense_entry]:
            print(key)
        #Thinking of adding a loop to check if the key selected includes a value or if its type(dict) then to print out all keys
        sub_category = input("This category has the stated selectable sub-categories. Would you like 1.Total 2.Gas 3.Electricity 4.Water: ").strip().title()
        if sub_category == "Total":
            print(sum(expenses_dict[user_view].values()))  # Prints the sum of values in Utilities
        elif sub_category == "Gas":
            print(f"The current value of {sub_category} is: {expenses_dict[expense_entry][sub_category]}")
        elif sub_category == "Electricity":
            print(f"The current value of {sub_category} is: {expenses_dict[expense_entry][sub_category]}")
        elif sub_category == "Water":
            print(f"The current value of {sub_category} is: {expenses_dict[expense_entry][sub_category]}")

    return expense_entry
#^^ This functions is mostly done but i think one missing item is to print out a list showing all totals like
# food: 100
# gas: 50

def total_threshold(search_amount, expenses_dict):

    #Will use to take user input and search for expense totals exceeding or equal to dependin on
    #user input
    pass

#Actual program running and variables
expenses_dict = {"Food": {"Groceries": 0, "Fast Food": 0},
            "Gas": 0,
            "Phone/Internet": 0,
            "Utilities": {"Gas":0, "Electricity": 0, "Water": 0},
             }

running = True

while running:
    try:
        choice = int(input("What would you like to do? 1.Enter Expense 2.View Totals 3.Print Listing 4.Quit: "))
        if choice == 1:
            expense_entry = input("Which category would you like to enter? 1.Food 2.Gas 3.Phone/Internet 4.Utilities: ").strip().title()
            # ^^ Thinking of changing this to strings to use them as the "key" ^^ and maybe have doulbe input. have if statment check string or int?
            enter_expenses(expense_entry, expenses_dict)
        elif choice == 2:
            user_view = input("Which category would you like to view? 1.Food 2.Gas 3.Phone/Internet 4.Utilities: ").strip().title()
            view_totals(user_view)
        elif choice == 3:
            print(expenses_dict)
        elif choice == 4:
            print("See you next time!")
            running = False
        else:
            print("You didn't enter a valid response. Please select from 1 to 4.")
            continue
    except:
        print("You didn't enter a number. Please select from 1 to 4.")
        continue
        #Testing clone

