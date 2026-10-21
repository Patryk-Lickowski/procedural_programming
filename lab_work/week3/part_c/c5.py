def loan_calculator():
    loan_amount = float(input("Enter the loan amount (e.g. 23000): "))
    annual_rate = float(input("Enter the annual interest rate (%): "))
    repayment_term = float(input("Enter how many years you will be paying this loan off for: "))

    if loan_amount <= 0 or repayment_term <= 0 or annual_rate < 0:
        print("Invalid loan amount / interest rate / repayment period entered")
        return

    r = annual_rate / 100 / 12
    n = repayment_term * 12

    if r == 0:
        # formula divides by zero at 0% interest, so just split the loan evenly
        monthly_repayment = loan_amount / n
    else:
        monthly_repayment = loan_amount * r * (1 + r) ** n / ((1 + r) ** n - 1)

    monthly_repayment = round(monthly_repayment, 2)
    total_amount = round(monthly_repayment * n, 2)
    total_interest = round(total_amount - loan_amount, 2)

    if monthly_repayment >= 500:
        print("Your monthly payments are high.")
    print(f"Monthly payment: £{monthly_repayment:.2f}")
    print(f"Total amount repaid: £{total_amount:.2f}")
    print(f"Total interest paid: £{total_interest:.2f}")


loan_calculator()