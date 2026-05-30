# My Monthly Expense Tracker
# Created by Saud Nawaz
# This project tracks my monthly expenses
# and tells me where I spend the most

import pandas as pd

# My expenses this month
data = {
    'Category': [
        'Food',
        'Transport',
        'Books',
        'Internet',
        'Clothing'
    ],
    'Amount_Spent': [
        3500,
        1200,
        1800,
        1000,
        2000
    ]
}

# Create table
df = pd.DataFrame(data)

# My monthly income
income = 15000

print("=" * 40)
print("   MY MONTHLY EXPENSE TRACKER")
print("   By: Saud Nawaz")
print("=" * 40)

# Show the table
print("\nMy Expenses This Month:\n")
print(df.to_string(index=False))

# Calculate total spent
total_spent = df['Amount_Spent'].sum()

# Calculate money left
money_left = income - total_spent

# Find highest expense
highest = df.loc[df['Amount_Spent'].idxmax(), 'Category']

# Find lowest expense
lowest = df.loc[df['Amount_Spent'].idxmin(), 'Category']

print("\n" + "=" * 40)
print("SUMMARY")
print("=" * 40)
print(f"Total Income   : Rs. {income}")
print(f"Total Spent    : Rs. {total_spent}")
print(f"Money Left     : Rs. {money_left}")
print(f"Highest Expense: {highest}")
print(f"Lowest Expense : {lowest}")

print("\n" + "=" * 40)
print("ADVICE")
print("=" * 40)

if money_left < 0:
    print("You spent more than your income!")
    print("Please reduce your expenses.")
elif money_left < 3000:
    print("You are saving very little.")
    print("Try to cut unnecessary expenses.")
else:
    print("Good job! You managed your budget well.")

print("\n" + "=" * 40)
print("   Done - by Saud Nawaz")
print("=" * 40)
