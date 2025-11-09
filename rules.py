# rules.py
def get_investment_allocation(age, income, risk, goal):
    allocations = {
        "Low": {"Equity": 20, "Debt": 60, "Gold": 10, "Cash": 10},
        "Moderate": {"Equity": 40, "Debt": 40, "Gold": 15, "Cash": 5},
        "High": {"Equity": 70, "Debt": 20, "Gold": 10, "Cash": 0}
    }

    alloc = allocations[risk].copy()

    # Age adjustment
    if age < 30:
        alloc["Equity"] += 10
        alloc["Debt"] -= 10
    elif age > 45:
        alloc["Equity"] -= 10
        alloc["Debt"] += 10

    # Goal adjustment
    if goal == "Short-term":
        alloc["Equity"] -= 10
        alloc["Debt"] += 10
    elif goal in ["Retirement", "Wealth Creation"]:
        alloc["Equity"] += 5
        alloc["Cash"] -= 5

    invest_amt = round(income * 0.25, -2)
    return alloc, invest_amt
