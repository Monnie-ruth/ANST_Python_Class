print ("Enter your monthly income")
monthly_income = int(input())
print ("Enter your total monthly expenses")
monthly_expenses = int(input())
monthly_savings = (monthly_expenses - monthly_income)
annual_interest_rate = 5
projected_savings = (monthly_savings * 12 + (monthly_savings * 12 * 0.05))
print (monthly_savings)
print (projected_savings)
