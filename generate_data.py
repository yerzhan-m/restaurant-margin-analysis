import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# 1. Setup Data Dictionaries (Imitating a Restaurant Menu)
menu = {
    'Margherita Pizza': {'category': 'Food', 'cost': 800, 'price': 2500},
    'Ribeye Steak': {'category': 'Food', 'cost': 3500, 'price': 9000},
    'Caesar Salad': {'category': 'Food', 'cost': 700, 'price': 2200},
    'Cappuccino': {'category': 'Beverage', 'cost': 200, 'price': 1200},
    'Craft Beer': {'category': 'Bar', 'cost': 400, 'price': 1500},
    'Signature Cocktail': {'category': 'Bar', 'cost': 600, 'price': 2500}
}

waiters = ['Yerzhan', 'Alina', 'Dias', 'Madina', 'Ruslan']
discounts = [0, 0, 0, 0.10, 0.15] # 10% and 15% loyalty discounts

# 2. Generate Synthetic Transactions
data = []
start_date = datetime(2026, 9, 1)

for i in range(10000):
    # Random date and time within a 60-day window
    random_days = random.randint(0, 60)
    random_hours = random.randint(10, 23) # Working hours 10:00 - 23:00
    random_minutes = random.randint(0, 59)
    tx_date = start_date + timedelta(days=random_days, hours=random_hours, minutes=random_minutes)
    
    item_name = random.choice(list(menu.keys()))
    qty = random.choice([1, 1, 1, 2, 3]) # Mostly 1 item per row, sometimes 2 or 3
    discount = random.choice(discounts)
    
    # Calculate financials
    gross_revenue = menu[item_name]['price'] * qty
    net_revenue = gross_revenue * (1 - discount)
    total_cost = menu[item_name]['cost'] * qty
    
    data.append([
        f"TXN-{10000 + i}", 
        tx_date.strftime("%Y-%m-%d %H:%M:%S"),
        random.choice(waiters),
        item_name,
        menu[item_name]['category'],
        qty,
        total_cost,
        net_revenue,
        discount
    ])

# 3. Create DataFrame and Export
columns = ['Transaction_ID', 'Date', 'Waiter', 'Item', 'Category', 'Quantity', 'Total_COGS', 'Net_Revenue', 'Discount_Pct']
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv('iiko_mock_sales.csv', index=False)
print("Dataset 'iiko_mock_sales.csv' successfully generated with 10,000 records!")