# Budget App
# Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment. These objects should allow for
# 1.  Depositing funds to each of the categories
# 2.  Withdrawing funds from each category
# 3.  Computing category balances
# 4.  Transferring balance amounts between categories

class budgetApp:
    features= ["Deposit","Withdraw", "bugdetBalance", "transferin", "transferout", "budgetBalance"]
    noOffeatures=len(features)

    def __init__ (self,budgetType, amtDeposited, amtWithdrawn, transferin, transferout, budgetBalance):
        
        self.budgetType=budgetType
        self.amtDeposited=amtDeposited
        self.amtWithdrawn=amtWithdrawn
        self.transferin=transferin
        self.transferout=transferout
        self.budgetBalance=budgetBalance
    
    def budgetCategory(self):
        print(" ************* You are currently in {} Budget***********".format(self.budgetType))
    def deposit(self):
        self.amtDeposited=int(input("Enter amount to be deposited in the budget \n"))
        print("Your deposit of {} is successful: ".format(self.amtDeposited))
        BudgetBal=self.amtDeposited
        print("Your budget balance is: {}".format(BudgetBal))

    def withdraw(self):
        self.amtWithdrawn=int(input("Enter amount to be withdrawan from budget \n"))
        print("Your have successfully withdrawn {} from your budget".format(self.amtWithdrawn))
        BudgetBal=self.amtDeposited-self.amtWithdrawn
        print("Your budget balance is: {}".format(BudgetBal))     

    def transferReceived(self):
        self.transferin=int(input("Enter amount to be transferred to this budget line \n"))
        print("Your have successfully transferred in {} to your {} budget".format(self.transferin, self.budgetType))
        BudgetBal=self.amtDeposited-self.amtWithdrawn+self.transferin
        print("Your budget balance is: {}".format(BudgetBal))

    def transferOutOfBudget(self):
        self.transferout=int(input("Enter amount to be transferred out of this budget line \n"))
        print("Your have successfully transferred out {} from your {} budget".format(self.transferout, self.budgetType))
        BudgetBal=self.amtDeposited-self.amtWithdrawn+self.transferin-self.transferout
        print("Your budget balance is: {}".format(BudgetBal))

    def remainingBudgetBal(self):
        BudgetBal=self.amtDeposited-self.amtWithdrawn+self.transferin-self.transferout
        print("Your budget balance is: {}".format(BudgetBal))

# Creating Object Food; Clothing & Entertainment
budgetFood = budgetApp("Food","","","","","")
budgetClothing = budgetApp("Clothing","","","","","")
budgetEntertainment = budgetApp("Entertainment","","","","","")

#Calling Properties
print("These are the available features: {}".format(budgetFood.features))
print("The number of available feature is: {}".format(budgetFood.noOffeatures))

#Testing with Food Object - Calling Methods
budgetFood.budgetCategory()
budgetFood.deposit()
budgetFood.withdraw()
budgetFood.transferReceived()
budgetFood.transferOutOfBudget()
budgetFood.remainingBudgetBal()

#Testing with Clothing Object - Calling Methods
budgetClothing.budgetCategory()
budgetClothing.deposit()
budgetClothing.withdraw()
budgetClothing.transferReceived()
budgetClothing.transferOutOfBudget()
budgetClothing.remainingBudgetBal()

#Testing with Entertainment Object - Calling Methods
budgetEntertainment.budgetCategory()
budgetEntertainment.deposit()
budgetEntertainment.withdraw()
budgetEntertainment.transferReceived()
budgetEntertainment.transferOutOfBudget()
budgetEntertainment.remainingBudgetBal()