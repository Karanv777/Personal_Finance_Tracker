
# 💰 Personal Finance Tracker

A simple yet powerful command-line based personal finance tracker built with Python. Keep track of your income, expenses, and savings — all stored in a convenient CSV file.


## 📌 Features

- 📝 Add transactions with:
  - Date (custom or default to today)
  - Amount
  - Category (Income/Expense)
  - Description
- 📅 View transactions within a selected date range
- 📊 See a summary: Total Income, Total Expense, and Net Savings
- 📁 CSV-based storage for portability and transparency



## 📁 Project Structure

```
Finance_Tracker/
├── finance_tracker.py       # Main application script
├── data_entry.py            # Helper functions for user input
└── finance_data.csv         # CSV log of all transactions

```


## 🛠️ Requirements

- Python 3.7+
- pandas

Install dependencies using pip:
```bash
pip install pandas
```


## 🚀 Getting Started

1. **Clone this repository**
```bash
git clone https://github.com/Karanv777/Personal_Finance_Tracker.git
cd Personal_Finance_Tracker
```

2. **Run the program**
```bash
python main.py
```


## 💡 Example Output

```
<<<<<<Financial Tracker>>>>>>
1. Add a new Transaction.
2. View transactions and summary within a range.
3. Exit

Transactions from 10/03/2025 to 30/03/2025:
 Date       Amount   Category   Description
10/03/2025  15000.0   Expense    Rent
12/03/2025 150000.0   Income     Dividend
23/03/2025 100000.0   Income     Sales
...

Summary:
Total Income : ₹350000.000
Total Expense : ₹215000.000
Net Savings: ₹135000.000

```

## 🧠 Future Improvements

- 📈 Add graphs (spending trends, category-wise breakdowns)
- 📂 Export reports (PDF/Excel)
- 🔎 Search by category or description keyword
- 🧮 Switch to SQLite for large-scale use
- 🖼️ GUI Version (Tkinter or PyQt)



## 👨‍💻 Author

Made with ❤️ by [Karanv777](https://github.com/Karanv777)
