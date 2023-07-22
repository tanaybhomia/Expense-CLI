from expense import Expense
import datetime
import calendar
import shutil

# Creates the Budget File for tracking the monthly budget 
def get_budget_from_user_or_file():
    budget_file_path = "budget.txt"
    try:
        with open(budget_file_path, "r") as budget_file:
            budget = float(budget_file.readline().strip())
    except (FileNotFoundError, ValueError):
        budget = None

    while budget is None:
        try:
            budget_input = input("Enter your monthly budget: ")
            budget = float(budget_input)
            with open(budget_file_path, "w") as budget_file:
                budget_file.write(str(budget))
        except ValueError:
            print("Invalid input. Please enter a valid monthly budget as a number.")

    return budget

# Takes the User input for an Expense 
def user_input():
	print(f"\n✍️ ENTER THE EXPENSE")
	expense_name = input("  I Bought :")
	expense_amount = float(input("  For Rupees :"))
	print(f"  You spent {expense_amount} on {expense_name}")

	# defining categories 
	expense_category = [
		"🍔 Food",
		"🏠 Home",
		"👕 Cloth",
		"💻 Work",
		"🎼 Fun",
		"🪣 Misc",
	]

	# for taking the category from the user
	while True:

		print("\n🔢 SELECT CATEGORY")
		for i,category_name in enumerate(expense_category):
			print(f"  {i+1} : {category_name}")

		value_range = f"[1 - {len(expense_category)}]"
		selected_index = int(input(f"Enter a Category {value_range} : ")) - 1
		if selected_index in range(len(expense_category)):
			selected_category = expense_category[selected_index]

			print("\n📝 ENTERED EXPENSE DETAILS")
			print(f"  Expense Name: {expense_name}")
			print(f"  Expense Amount: {expense_amount}")
			print(f"  Expense Category: {selected_category}")
			confirm = input("\nENTER THIS RESPONSE (yes/no): ")

			if confirm.lower() == "yes":
				newexpense = Expense(name = expense_name,category= selected_category,amount=expense_amount)
				return newexpense
			else :
				break
		else : 
			print("Invalid Entry, Please try again")

# Saves the content to the CSV file
def savetofile(expense : Expense,expense_file_path):
	print(f"\n📁 SAVING USER EXPENSE : {expense}")
	with open(expense_file_path,"a", encoding = 'utf-8') as f:
		f.write(f"{expense.name},{expense.category},{expense.amount}\n")
	pass

# Shows the Summary of the Spending
def summaries(expense_file_path,budget):
	print(f"\n📓 SUMMARY")
	expenses = []
	with open(expense_file_path , "r" , encoding='utf-8') as f:
		lines = f.readlines()
		for line in lines:
			expense_name,expense_category,exepense_amount = line.strip().split(",")
			line_expense = Expense(
				name = expense_name,
				category = expense_category,
				amount = float((exepense_amount))
			)
			expenses.append(line_expense)
	
	amount_by_category = {} 
	for expense in expenses:
		key = expense.category
		if key in amount_by_category:
			amount_by_category[key] += expense.amount
		else:
			amount_by_category[key] = expense.amount

	print("Expenses by Category")
	for category,amount in amount_by_category.items():
		print(f"  {category}:,{amount:.2f}₹")
	
	total = float(sum(amount_by_category.values()))
	remaining_budget = budget-total
	print(f"\n🎰 You have spent a total of {total}")
	if remaining_budget <= 0:
		print(f"🫠 You have already spent over the budget")
	else :
		print(f"🎫 Remaining Budget {remaining_budget}")

def main_menu():
    print("\n✅ WHAT DO YOU WANT TO DO") 
    print("  1. 💸 Enter an Expense")
    print("  2. 📓 Show Summary")
    print("  3. 🔴 Exit")

def main():
    print(r'''
 ______                                  _______             _
|  ____|                                |__   __|           | |
| |__  __  ___ __   ___ _ __  ___  ___     | |_ __ __ _  ___| | _____ _ __
|  __| \ \/ / '_ \ / _ \ '_ \/ __|/ _ \    | | '__/ _` |/ __| |/ / _ \ '__|
| |____ >  <| |_) |  __/ | | \__ \  __/    | | | | (_| | (__|   <  __/ |
|______/_/\_\ .__/ \___|_| |_|___/\___|    |_|_|  \__,_|\___|_|\_\___|_|
            | |
            |_|  
    ''')
    
    # Creates the Budget file 
    budget = get_budget_from_user_or_file()
    
    # Creates the Expenses Database
    expense_file_path = "expense.csv"
    
    while True:
        main_menu()
        choice = input("-> ")

        if choice == "1":
            # Takes the user input
            expense = user_input()

            # Saves the input to the file
            savetofile(expense, expense_file_path)

        elif choice == "2":
            # Rd the file and then show the summary
            summaries(expense_file_path, budget)
        elif choice == "3":
            print("EXITING THE EXPENSE TRACKER! BYE 🖐️")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

if __name__ == "__main__":
	main()