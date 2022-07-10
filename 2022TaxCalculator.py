# This is a federal income tax calculator
print("Welcome to the 2022 federal income tax calculator\n Note this ONLY calculates federal income tax and not state or local taxes!\n Standard tax deductions are automatically applied, at the moment this calculator does not accomodate itemized deductions.\n This could mean you may qualify for lower federal tax or a higher refund.\n Please have the following ready: Your 2022 income and if applicable your spouse's 2022 income.")
income = 0
income_tax = 0
other_income = 0
capital_losses = 0
filing_jointly = False
filing_status = input("\nAre you filing taxes as a married couple filing jointly? Yes or No:\n")
if filing_status == "Yes":
    filing_jointly = True
else:
    filing_jointly = False
your_income = float(input("\nEnter your work income for 2022:\n"))
withheld_byemployer = float(input("Has any of your income been withheld by your employer for federal taxes?\nIf no enter 0, if yes enter the amount withheld:\n"))
other_income = float(input("Do you have income from other sources such as capital gains, unemployment income, or other taxable income? If no enter 0, if yes enter how much:\n"))
capital_losses = float(input("Do you have capital losses? If no enter 0, if yes enter amount:\n"))
if capital_losses < 3000:
    capital_losses = capital_losses
else:
    capital_losses = 3000
your_income = your_income + other_income - capital_losses
if your_income <= 10275:
    your_income = your_income - 12950
    income_tax = your_income * 0.1
elif your_income <= 41775:
    income_tax = your_income * 0.12
elif your_income <= 89075:
    income_tax = your_income * 0.22
elif your_income <= 170050:
    income_tax = your_income * 0.24
elif your_income <= 215950:
    income_tax = your_income * 0.32
elif your_income <= 539900:
    income_tax = your_income * 0.35
else:
    income_tax = your_income * 0.37
if filing_jointly == False:
    print("Calculating...")
else:
    spouse_income = float(input("\nEnter your spouse's work income:\n"))
    withheld_byemployer2 = float(input("Has any of your spouse's income been withheld by their employer for federal taxes?\nIf no enter 0, if yes enter the amount withheld:\n"))
    other_income = float(input("Does your spouse have income from other sources such as capital gains, unemployment income, or other taxable income?\nIf no enter 0, if yes enter how much:\n"))
    capital_losses = float(input("Does your spouse have capital losses?\nIf no enter 0, if yes enter amount:\n"))
    if capital_losses < 3000:
        capital_losses = capital_losses
    else:
        capital_losses = 3000
    spouse_income = spouse_income + other_income - capital_losses
    total = your_income + spouse_income - 25900
    if total <= 20550:
        income_tax = total * 0.1
    elif total <= 83550:
        income_tax = total * 0.12
    elif total <= 178150:
        income_tax = total * 0.22
    elif total <= 340100:
        income_tax = total * 0.24
    elif total <= 431900:
        income_tax = total * 0.32
    elif (total <= 647850):
        income_tax = total * 0.35
    else:
        income_tax = (total * 0.37) - (withheld_byemployer + withheld_byemployer2)
if income_tax > 0:
    print("\nYour federal income tax for 2022 is: " + str(income_tax))
else:
    print("\nYour federal income tax refund for 2022 is: " + str(abs(income_tax)))