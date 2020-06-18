def endBalance(balance, annualInterestRate, fixedMonthlyPayment):
    for i in range(12):
        MonthlyInterestRate= (annualInterestRate) / 12.0
        MonthlyUnpaidBalance = (balance) - (fixedMonthlyPayment)
        balance = (MonthlyUnpaidBalance) + (MonthlyInterestRate * MonthlyUnpaidBalance)
    # print("Remaining balance: ", round(balance, 2))
    return round(balance, 2)

fixedMonthlyPayment = 10
while True:
    if endBalance(balance, annualInterestRate, fixedMonthlyPayment) < 0:
        print("Lowest Payment: ", fixedMonthlyPayment)
        break
    else: 
        fixedMonthlyPayment += 10
