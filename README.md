# 📊 Sales Performance Dashboard

> **Created by Rushikesh Desai**  
> B.Tech — Computer Science & Engineering  
---

## 🔎 Project Overview

This project is an **interactive retail Sales Performance Dashboard** built using **Python (Pandas, NumPy)** for data analysis and a fully responsive **HTML/CSS/JavaScript** front end for visualization — replicating the kind of business intelligence dashboards built with Power BI.

The dashboard analyzes a retail dataset covering **144 transactions** across **12 months (Jan–Dec 2024)**, providing actionable insights on revenue, profit, regional performance, and discount impact.

---

## 📸 Dashboard Preview

![Dashboard Preview](assets/preview.png)

> Open `dashboard/index.html` in any browser to view the live interactive dashboard.

---

## ✨ Key Features

| Feature | Details |
|---|---|
| 📈 Monthly Trend | Sales vs Profit line chart across 12 months |
| 📦 Category Analysis | Electronics, Furniture, Clothing breakdown |
| 🌍 Regional Breakdown | North, South, East, West comparison |
| 🏆 Top Products | Ranked by total sales revenue |
| 💸 Discount Impact | How discounts affect average profit |
| 🎛️ Live Filters | Filter by Region and Category interactively |
| 📊 5 KPI Cards | Total Sales, Profit, Orders, Margin, Discount |

---

## 📊 Key Insights from Analysis

- **Total Sales:** ₹34.6 Lakh across 144 orders
- **Total Profit:** ₹5.89 Lakh | **Profit Margin:** 17.0%
- **Top Category:** Electronics (₹19.72L — 57% of total sales)
- **Top Product:** Laptop (₹10L revenue, 11 orders)
- **Best Month:** November (₹3.37L sales)
- **Discount Impact:** High discounts (>10%) reduce avg profit by **85%** vs no-discount orders

---

## 🛠️ Tech Stack

```
Python 3.x      → Data analysis engine
├── Pandas      → Data loading, grouping, aggregation
├── NumPy       → Numerical computations
└── JSON        → Data export for dashboard

HTML / CSS / JS → Interactive frontend dashboard
└── Chart.js    → Bar, Line, Doughnut charts
```

---

## 📁 Project Structure

```
sales-performance-dashboard/
│
├── 📂 data/
│   └── retail_sales.csv          ← Raw retail dataset (144 records)
│
├── 📂 scripts/
│   └── analyze_sales.py          ← Python analysis script (by Rushikesh Desai)
│
├── 📂 dashboard/
│   ├── index.html                ← Interactive dashboard (open in browser)
│   └── sales_data.json           ← Generated KPI data (output of script)
│
├── 📂 assets/
│   └── preview.png               ← Dashboard screenshot
│
└── README.md
```

---

## 🚀 How to Run

### Option 1 — Open Dashboard Directly
```bash
# Just open in browser — no installation needed!
open dashboard/index.html
```

### Option 2 — Run Python Analysis First
```bash
# Step 1: Install dependencies
pip install pandas numpy

# Step 2: Run the analysis
python scripts/analyze_sales.py

# Step 3: Open the dashboard
open dashboard/index.html
```

---

## 📈 Dataset Description

| Column | Description |
|---|---|
| Order_ID | Unique order identifier |
| Date | Order date (Jan–Dec 2024) |
| Category | Electronics / Furniture / Clothing |
| Product | Specific product name |
| Region | North / South / East / West |
| Sales | Total sales amount (₹) |
| Quantity | Number of units sold |
| Discount | Discount applied (0 to 0.15) |
| Profit | Profit earned (₹) |

---

## 🎓 Skills Demonstrated

- ✅ Data loading and cleaning with **Pandas**
- ✅ Aggregation and grouping (by category, region, month)
- ✅ KPI calculation (Total Sales, Profit Margin, Avg Discount)
- ✅ **Data visualization** — interactive charts (line, bar, doughnut)
- ✅ Filter-based dynamic reporting (Region / Category filters)
- ✅ End-to-end project from raw CSV to interactive dashboard

---

## 🔗 Connect with Me

- 💼 [LinkedIn](https://www.linkedin.com/in/rushikesh-desai-6813102a4/)
- 💻 [GitHub](https://github.com/rushikeshdesai22)
- 📧 [rushikeshdesai2022@gmail.com](mailto:rushikeshdesai2022@gmail.com)
- 📍 Navi Mumbai, India

---

*Built with Python, Pandas, and Chart.js — Rushikesh Desai © 2024*
