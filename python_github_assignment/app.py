# Display assignment welcome message
print("Welcome to my Python Github Assignment!")

# Create input for monthly spending and convert to float with error handling for non-numeric inputs
while True:
    monthly_spending = input("How much did you spend this month?")  
    try:
        monthly_spending = float(monthly_spending)
        break
    except ValueError:
        print("Please enter a valid number for your monthly spending.")

# Calculate yearly spending using monthly spending
yearly_spending = monthly_spending * 12

# Print yearly spending message and respond to user
print(f"With your current monthly spending, you are on track to spend {yearly_spending} dollars this year!")



