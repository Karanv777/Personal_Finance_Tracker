import matplotlib, pandas as pd , csv
from datetime import datetime
from Data_entry import get_date, get_description, get_category, get_amount


class CSV :
    CSV_FILE = "finance_data.csv"
    COLUMNS =  ["Date", "Amount", "Category", "Description"]
    FORMAT = "%d/%m/%Y"

    @classmethod
    def initialize_csv(cls) -> None:
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns = cls.COLUMNS) # DataFrame is an object in pandas that allows us to access different rows and coloumns from a file
            df.to_csv(cls.CSV_FILE, index=False) # This is used to save or convert the data to a csv file
            print("CSV file created")
    
    @classmethod
    def write_entry(cls, date, amount, category, description) -> None:
        new_entry = {
            "Date" : date,
            "Amount" : amount,
            "Category" : category,
            "Description" : description
        }
        csvfile = open(cls.CSV_FILE, "a", newline="")
        writer = csv.DictWriter (csvfile, fieldnames = cls.COLUMNS) # It means we are taking a dictionary and writing it into a csv file. So, DictWriter is doing that.
        writer.writerow(new_entry)
        csvfile.close()

        print("Entry Added Successfully")

    @classmethod
    def get_transactions(cls, start_date, end_date): # For fetching transactions between a date range
        df = pd.read_csv(cls.CSV_FILE)
        df["Date"] = pd.to_datetime(df["Date"], format = CSV.FORMAT) # In PANDAS you can access individual rows and as well as columns
        start_date = datetime.strptime(start_date, CSV.FORMAT) # This is used to take the string and then parse it as a datetime object
        end_date = datetime.strptime(end_date, CSV.FORMAT) # we are doing this so that we can compare it with the date in the csv file which we cannot do with string.
        
        # Mask is something that we can apply to the different rows inside of a dataframe.
        mask = (df["Date"] >= start_date) & (df["Date"] <= end_date) # This is checking if the data in the current row in the column date is greater than thr start date or it less than than the end date.
        filtered_df = df.loc[mask] # This will locate and return a filtered dataframe that only contains the rows where the mask is True.

        if filtered_df.empty:
            print(f"No transactions found between {start_date.strftime(CSV.FORMAT)} and {end_date.strftime(CSV.FORMAT)}.")
        else:
            print(f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}:")

            print(
                    filtered_df.to_string( index = False, formatters = {"Date" : lambda x: x.strftime(CSV.FORMAT)})
                 ) # If we want to format it differently than we can put a function we want to apply to every single element inside the column If we want to format it differently.
            
            total_income = filtered_df[filtered_df["Category"] == "Income"]["Amount"].sum()
            total_expense = filtered_df[filtered_df["Category"] == "Expense"]["Amount"].sum()
            print("\nSummary: ")
            print(f"Total Income : ₹{total_income:.3f}") # ":.3f" is used to format the number to 3 decimal places
            print(f"Total Expense : ₹{total_expense:.3f}")
            print(f"Net Savings: ₹{(total_income - total_expense):.3f}")

def add():
    CSV.initialize_csv()
    date = get_date("Enter the date in {DD/MM/YYYY} or Press enter for current date: ", allow_default= True)
    amount = get_amount()
    categoty = get_category()
    description = get_description()
    CSV.write_entry(date, amount, categoty, description)
        
def main():
    try: 
        while True:
            print("\n<<<<<<Financial Tracker>>>>>>")
            print("1. Add a new Transaction.\n2. View transactions and summary within a range.\n3. Exit")
            ch = int(input("Enter your choice {1-3}: "))

            if ch == 1:
                add()
            
            elif ch == 2:
                strt_Date = get_date("From [DD/MM/YYYY]: ")
                end_Date = get_date("To [DD/MM/YYYY]: ") 
                print("\n")
                df = CSV.get_transactions(strt_Date, end_Date)

            else:
                cnf_ex = input("Do you want to Exit!\n").strip().upper()
                if cnf_ex in ['Y']:
                    print("Exiting.....")
                    break

    except ValueError :
        print("Invalid Input! Enter choice between {1-3}.")
            

if __name__ == "__main__" : 
    main()
