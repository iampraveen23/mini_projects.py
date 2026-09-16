# Storing the data
expenses = []

# adding the data
def add_expense():

    #Handles error if value is not valid
    try:
        amount = int(input("Enter Amount(Rs) : "))
    except ValueError:
        print("Please enter a valid number.")
        return
    # Amount should be greater than 0 else prints the below statement
    if  amount <= 0:
        print(f"{amount} is not a valid number. Please Enter correct number. ")
        return
    
    category = input("Enter Category (i.e)food : ")
    Description = input("Enter Description (i.e)Lunch :")

# Appending the data to the list
    expense = {
        "Amount":amount,
        "category": category,
        "Description":Description
    }

    expenses.append(expense)

# To view the expenses    
def view_expense():

    # If the list is empty, it throws the below statement
    if not expenses:
        print("You don't have data to display ! Please add data.")

    for expense in expenses:
        print(f"Amount:{expense['amount']}")
        print(f"Category:{expense['category']}")
        print(f"Description:{expense['Description']}")

# Calculates the expenses        
def calculate_amount():

    # If the expenses have no data, the below statement prints
    if not expenses:
        print("No expenses found. Please add an expense first.")
        return 
    
    else:
        total_expenses = 0
        for expense in expenses:
            total_expenses = total_expenses + expense["amount"]
        print(f"Total expense {total_expenses}")

#MENU:-
while True:
    print("====================EXPENSE TRACKER======================")
    print("1. ADD EXPENSE")
    print("2. VIEW EXPENSE")
    print("3. CALCULATE TOTAL EXPENSES")
    print("4. EXIT")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_expense()

    if choice == "2":
        view_expense()

    if choice == "3":
        calculate_amount()

    if choice == "4":
        break

# If the user enters other than the number, that is displayed the below statement prints 
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please enter 1 to 4.")



