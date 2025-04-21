from datetime import datetime

date_format = "%d/%m/%Y"

CATEGORIES = {"I" : "Income", "E" : "Expense"}

def get_date(prompt, allow_default = False): # prompt is what we are going to ask the user to input before they give us a date and allow_default is if user want to input current date by enter 
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try :
        valid_date = datetime.strptime(date_str, date_format)
        return  valid_date.strftime(date_format)
    
    except ValueError:
        print("Invalid date format. Please use DD/MM/YYYY format.")
        return get_date(prompt, allow_default)


def get_amount():
    try:
        amount = float(input("Enter the Amount : "))
        if amount <= 0:
                raise ValueError('Invalid amount. Please enter a "Positive Value".')
        return amount
    
    except ValueError :
        print(ValueError)
        return get_amount()
    

def get_category():
    category = input("Enter the Category ['I' for Income or 'E' of Expense]: ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Invalid Category. Please enter 'I' for Income or 'E' for Expense.")
    return get_category()
        
    

def get_description():
    description = input("Enter the Description {optional} : ")
    return description