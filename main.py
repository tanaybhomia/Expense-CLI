from expense import Expense


def main():
    print("💸 This is a Expense Tracker!")
    
	# Creating the User File 
    expense_file_path = "expense.csv"
    
	# Takes the user input 
    # expense = user_input()
    
	# Saves the input to the file
    # savetofile(expense,expense_file_path)
    
	# Rd the file and then show the summmary
    summaries(expense_file_path) 
    pass

def user_input():
	print(f"✍️ Enter the expense")
	expense_name = input("Enter Expense Name :")
	expense_amount = float(input("Enter the Amount :"))
	print(f"You have Entered {expense_name} and {expense_amount}")

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

		print("Select type")
		for i,category_name in enumerate(expense_category):
			print(f"  {i+1} : {category_name}")

		value_range = f"[1 - {len(expense_category)}]"
		selected_index = int(input(f"Enter a Category {value_range} : ")) - 1
		if selected_index in range(len(expense_category)):
			selected_category = expense_category[selected_index]
			newexpense = Expense(name = expense_name,category= selected_category,amount=expense_amount)
			return newexpense
		else : 
			print("Invalid Entry, Please try again")

def savetofile(expense : Expense,expense_file_path):
	print(f"📁 Saving User Expense : {expense} to {expense_file_path}")
	with open(expense_file_path,"a", encoding = 'utf-8') as f:
		f.write(f"{expense.name},{expense.category},{expense.amount}\n")
	pass

def summaries(expense_file_path,budget):
	print(f"📓 Summary ")
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

	print("Expenses by Category 📈")
	for category,amount in amount_by_category.items():
		print(f"	{category}:,{amount:.2f}₹")

if __name__ == "__main__":
	main()

