for i in range(12):
    MonthlyInterestRate= (annualInterestRate) / 12.0
    MinimumMonthlyPayment = (monthlyPaymentRate) * (balance)
    MonthlyUnpaidBalance = (balance) - (MinimumMonthlyPayment)
    balance = (MonthlyUnpaidBalance) + (MonthlyInterestRate * MonthlyUnpaidBalance)

print("Remaining balance: ", round(balance, 2))
