# 📊 Restaurant POS Analytics: Margin Optimization & Cross-Subsidization

## 🎯 Executive Summary
**Business Problem:** The restaurant faces margin compression due to the high baseline COGS of premium perishable items (e.g., Ribeye Steak) and the financial impact of loyalty program discounts.
**Project Goal:** To model a synthetic POS dataset (imitating iiko TMS OLAP reports) and analyze transaction-level data to identify margin leaks.
**Key Business Outcome:** Identified a ~2% net margin loss caused by applied discounts. Formulated a cross-subsidization strategy: utilizing targeted discounts on premium items to prevent 100% spoilage write-offs, while aggressively offsetting the margin loss by promoting high-margin Bar & Beverage categories.

## 🛠 Data Architecture & Tech Stack
- **Language:** Python (Pandas, NumPy)
- **Environment:** Jupyter Notebook (VS Code)
- **Data Source:** Custom Python script generating 10,000 realistic synthetic POS transactions (incorporating menu pricing, randomized time-series data, and staff discount logic).

## 🔍 Methodology
1. **Data Engineering:** Developed a Python generator using the `datetime` and `random` libraries to synthesize a dataset reflecting realistic restaurant operations and unit economics.
2. **Exploratory Data Analysis (EDA):** Calculated baseline metrics including Gross Revenue, Net Revenue, and overall Food Cost %.
3. **Financial Modeling:** Segmented profitability by menu categories and quantified the exact monetary value lost to the discount program.

## 💡 Actionable Insights & Business Recommendations
* **Insight 1 (Inventory Management):** Premium items like Ribeye Steak drive significant revenue but carry a high baseline COGS. Strategic discounting on these items is a validated spoilage mitigation tactic, preventing complete financial write-offs of perishable inventory.
* **Insight 2 (Margin Optimization):** The overall net margin drops by ~2% strictly due to applied staff/loyalty discounts. 
    * *Recommendation:* Offset this margin loss through cross-subsidization. Increase marketing and staff incentive focus on high-margin categories (Bar & Beverages) to balance the overall unit economics and protect the target 28-30% Food Cost threshold.

---
*Designed by Yerzhan Mushkenov — Data Analyst merging operational management with data-driven insights.*# restaurant-margin-analysis
