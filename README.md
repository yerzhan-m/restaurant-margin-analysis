# Restaurant Margin & Staff Performance Analysis

## Overview
This repository contains a data analytics project focused on the Food & Beverage (F&B) sector. The primary objective is to analyze restaurant unit economics, evaluate staff performance, and identify areas for cost optimization using SQL and Python.

The analysis is based on a synthesized dataset simulating 10,000 transactions from a typical restaurant POS system (e.g., iiko or r-keeper). 

**Key Business Goals:**
- Calculate total revenue and ideal vs. actual Food Cost (COGS).
- Analyze the financial impact of loyalty discounts on overall profitability.
- Evaluate server performance based on total revenue generation, average check size, and discount utilization.
- Detect potential anomalies or fraudulent behavior in discount applications.

## Technical Stack
- **Languages:** Python 3, SQL
- **Libraries:** pandas, sqlite3, numpy
- **Data Source:** Synthetic dataset (`iiko_mock_sales.csv`) generated via `generate_data.py`.

## Project Structure
- `generate_data.py`: A Python script using `pandas` and `numpy` to generate a realistic mock dataset of POS transactions.
- `analysis.ipynb`: A Jupyter Notebook containing the end-to-end data pipeline, including data loading, SQL querying (via in-memory SQLite), and metric calculation.
- `iiko_mock_sales.csv`: The generated dataset containing transaction details (Date, Waiter, Item, Category, Quantity, COGS, Net Revenue, Discount Percentage).

## Key Insights & Analytics

### 1. Overall Profitability Impact
The core of the analysis compares the ideal food cost (without discounts) against the actual food cost to reveal the margin lost.

- **Gross Revenue (Pre-Discount):** 50,760,900 KZT
- **Net Revenue (Actual):** 48,213,240 KZT
- **Total COGS:** 16,692,100 KZT
- **Lost to Discounts:** 2,547,660 KZT
- **Ideal Food Cost:** 32.88%
- **Actual Food Cost:** 34.62%
- **Margin Lost to Discounts:** 1.74%

### 2. Category Performance
Revenue and Food Cost vary significantly by product category:

| Category | Total Revenue (KZT) | Total COGS (KZT) | Food Cost % |
| :--- | :--- | :--- | :--- |
| Food | 35,038,010 | 13,485,900 | 38.49% |
| Bar | 10,189,750 | 2,682,400 | 26.32% |
| Beverage | 2,985,480 | 523,800 | 17.54% |

### 3. Server Performance & Discount Audit
The SQL queries evaluate staff performance not just by revenue, but by how frequently they apply discounts. 

**Top Performers (by Net Revenue):**
1. **Dias:** 9,909,615 KZT (Avg Check: 4,815 KZT, Discount Freq: 38.4%)
2. **Yerzhan:** 9,745,590 KZT (Avg Check: 4,907 KZT, Discount Freq: 39.7%)
3. **Ruslan:** 9,694,685 KZT (Avg Check: 4,830 KZT, Discount Freq: 40.4%)

**Fraud Investigation (Ruslan):**
A targeted SQL audit on the server "Ruslan" (who had the highest discount frequency) analyzed his discount applications by hour of the day. The analysis reveals peak discount application during the 14:00 and 19:00 hours, warranting further operational review for potential abuse of loyalty programs during peak shifts.

## How to Run the Project
1. Run `python generate_data.py` to recreate the `iiko_mock_sales.csv` dataset.
2. Open and run all cells in `analysis.ipynb` to view the full SQL and pandas outputs.
