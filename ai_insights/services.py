from django.db.models import Sum

def generate_insights(expenses):
    if not expenses:
        return ["No expenses found"]

    # Total spending
    total = sum(exp.amount for exp in expenses)

    # Category breakdown
    category_totals = {}
    for exp in expenses:
        category_totals[exp.category] = category_totals.get(exp.category, 0) + exp.amount

    # Highest spending category
    top_category = max(category_totals, key=category_totals.get)
    top_amount = category_totals[top_category]

    insights = []

    # Insight 1
    insights.append(f"You spent a total of ₹{total}")

    # Insight 2
    insights.append(f"Your highest spending is on {top_category} (₹{top_amount})")

    # Insight 3 (percentage)
    percent = (top_amount / total) * 100
    insights.append(f"{top_category} accounts for {percent:.2f}% of your spending")

    # Insight 4 (warning)
    if percent > 50:
        insights.append(f"You are heavily spending on {top_category}. Consider reducing it.")

    # Insight 5 (savings suggestion)
    savings = top_amount * 0.2
    insights.append(f"You could save around ₹{int(savings)} by cutting 20% of {top_category}")

    return insights