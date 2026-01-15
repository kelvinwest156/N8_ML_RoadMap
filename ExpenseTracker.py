# create oe open csv
# with open("expenses.csv", "a") as file:
#    file.write("Date,Description,Amount\n")

# add expenses
# date = input("Enter date (YYYY-MM-DD): ")
# desc = input("Enter description: ")
# amount = input("Enter amount: ")

# with open("expenses.csv", "a") as file:
#     file.write(f"{date},{desc},{amount}\n")

# print("Expense saved.")

# view expenses
with open("expenses.csv", "r") as file:
    for line in file:
        print(line.strip())
