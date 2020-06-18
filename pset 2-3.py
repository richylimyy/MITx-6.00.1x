def endBalance(balance, monthlyInterestRate, fixedMonthlyPayment):
    for i in range(12):
        MonthlyUnpaidBalance = (balance) - (fixedMonthlyPayment)
        balance = (MonthlyUnpaidBalance) + (monthlyInterestRate * MonthlyUnpaidBalance)
    # print("Remaining balance: ", round(balance, 2))
    return round(balance, 2)

monthlyInterestRate = annualInterestRate/12
low = balance/12
high = (balance * (1 + monthlyInterestRate)**12)/12
n = 0

while True:
    monthlyPay = (low + high)/2
    endBal = endBalance(balance, monthlyInterestRate, monthlyPay)
    # print(low, high, monthlyPay, endBal)
    if endBal > 0:
        low = monthlyPay
    elif endBal < 0.05:
        high = monthlyPay
    if -0.05 <= endBal <= 0: 
        print("Lowest Payment: " , round(monthlyPay, 2))
        break
