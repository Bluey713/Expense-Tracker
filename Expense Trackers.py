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

#Functions should only have one task, they should not be asking for input

#import sys
expense_list = ["Food", "Gas", "Insurance", "Property Tax", "Utilities"] #"Groceries", "Fast Food"
#Still need to thing about how to incorporate lists. So far im just using a giant dictionary




#Functions

def user_choice():
    #This is the starting point of the whole loop. Will take user input to see if the want to add or view
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


def enter_expenses():
    #This will be the main function to take the user input and properly allocate expenses
    if expense_entry == "Food":
        for key in expenses_dict["Food"]:
            print(key)
        #Thinking of adding a loop to check if the key selected includes a value or if its type(dict) then to print out all keys
        sub_category = input("This category has the stated selectable sub-categories. Which do you want to access: ").strip().title()
        if sub_category == "Groceries":
            amount = float(input("Enter the amount of the expense for Groceries: ")) #maybe switch these to f strings and include the key
            expenses_dict[expense_entry][sub_category] += amount
            print(f"The updated value of {sub_category} is: {expenses_dict[expense_entry][sub_category]}")
            return True

        elif sub_category == "Fast Food":
            amount = float(input("Enter the amount of the expense for Fast Food: "))
            expenses_dict[expense_entry][sub_category] += amount
            print(f"The updated value of {sub_category} is: {expenses_dict[expense_entry][sub_category]}")
            # return True
            #^^ Need to figure out how to make the program keep looping after the print statement. Tried adding return True as a test but no.
    elif expense_entry == 2:
        #If 2 and no sub-category
        #input from user as float
        #expenses[
        #
        pass
    elif expense_entry == 3:
        pass
    elif expense_entry == 4:
        pass

def continue_entering():
    pass
    #is this function required to keep the program running?
    #was thinking of having additional print statements asking to continue or print out stuff which would just call the previous functions



def view_totals():
    #Will use this to ask user which expense account or sub account the want to view
    user_view = input("Which total would you like to view: ")
    pass

def total_threshold():
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
        choice = int(input("What would you like to do? 1.Enter Expense 2.View Totals 3.Quit: "))
        if choice == 1:
            expense_entry = input("Which category would you like to enter? 1.Food 2.Gas 3.Phone/Internet 4.Utilities: ").strip().title()
            # ^^ Thinking of changing this to strings to use them as the "key" ^^ and maybe have doulbe input. have if statment check string or int?
        elif choice == 2:
            view_totals()
        elif choice == 3:
            print("See you next time!")
            running = False
        else:
            print("You didn't enter a valid response. Please select from 1 to 3.")
            continue
    except:
        print("You didn't enter a number. Please select from 1 to 3.")
        continue

