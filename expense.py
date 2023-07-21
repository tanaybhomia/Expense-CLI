# class file for storing the functions and other attributes 

class Expense :
    
	def __init__(self,name,category,amount) -> None:
		self.name = name
		self.category = category
		self.amount = amount

	def __repr__(self):
		return f"{self.name} , {self.amount:.2f}₹ , {self.category} "