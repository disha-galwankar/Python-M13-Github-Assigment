print("Welcome to my Python Github Assignment!")

monthly_spending = input("How much did you spend this month?")

monthly_spending = float(monthly_spending)
yearly_spending = monthly_spending * 12

print(f"With your current monthly spending, you are on track to spend {yearly_spending} dollars this year!")

try:
    monthly_spending = float(monthly_spending)
except ValueError:
    print("Please enter a valid number for your spending.")
    exit()

