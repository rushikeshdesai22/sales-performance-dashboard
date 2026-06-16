"""
=============================================================
  Sales Performance Dashboard - Data Analysis Script
  Author  : Rushikesh Desai
  Email   : rushikeshdesai2022@gmail.com
  GitHub  : https://github.com/rushikeshdesai22
  LinkedIn: https://www.linkedin.com/in/rushikesh-desai-6813102a4/
  College : SSIEMS (DBATU Lonere), Parbhani
  Tools   : Python, Pandas, NumPy
=============================================================
  Description:
    This script analyzes a retail sales dataset to generate
    key performance indicators (KPIs) and data summaries
    that power the interactive Sales Performance Dashboard.
=============================================================
"""

import pandas as pd
import numpy as np
import json
import os

# ── Load Dataset ──────────────────────────────────────────────
print("=" * 60)
print("  Sales Performance Dashboard | Created by Rushikesh Desai")
print("=" * 60)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv(os.path.join(BASE_DIR, "data", "retail_sales.csv"))
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.strftime("%b")
df["Month_Num"] = df["Date"].dt.month

print(f"\n✅ Dataset loaded: {len(df)} records | {df['Date'].min().date()} → {df['Date'].max().date()}")

# ── KPI Summary ───────────────────────────────────────────────
total_sales   = df["Sales"].sum()
total_profit  = df["Profit"].sum()
total_orders  = len(df)
avg_discount  = df["Discount"].mean() * 100
profit_margin = (total_profit / total_sales) * 100

print("\n📊 KEY PERFORMANCE INDICATORS")
print("-" * 40)
print(f"  Total Sales    : ₹{total_sales:,.0f}")
print(f"  Total Profit   : ₹{total_profit:,.0f}")
print(f"  Total Orders   : {total_orders}")
print(f"  Avg Discount   : {avg_discount:.1f}%")
print(f"  Profit Margin  : {profit_margin:.1f}%")

# ── Sales by Category ─────────────────────────────────────────
cat_summary = df.groupby("Category").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order_ID", "count")
).reset_index().sort_values("Sales", ascending=False)

print("\n📦 SALES BY CATEGORY")
print("-" * 40)
print(cat_summary.to_string(index=False))

# ── Sales by Region ───────────────────────────────────────────
region_summary = df.groupby("Region").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
).reset_index().sort_values("Sales", ascending=False)

print("\n🌍 SALES BY REGION")
print("-" * 40)
print(region_summary.to_string(index=False))

# ── Monthly Trend ─────────────────────────────────────────────
monthly = df.groupby(["Month_Num", "Month"]).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
).reset_index().sort_values("Month_Num")

print("\n📅 MONTHLY TREND")
print("-" * 40)
print(monthly[["Month", "Sales", "Profit"]].to_string(index=False))

# ── Top 5 Products ────────────────────────────────────────────
top_products = df.groupby("Product").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order_ID", "count")
).reset_index().sort_values("Sales", ascending=False).head(5)

print("\n🏆 TOP 5 PRODUCTS BY SALES")
print("-" * 40)
print(top_products.to_string(index=False))

# ── Discount Impact ───────────────────────────────────────────
df["Discount_Band"] = pd.cut(
    df["Discount"],
    bins=[-0.01, 0.001, 0.10, 0.20],
    labels=["No Discount", "Low (≤10%)", "High (>10%)"]
)
discount_impact = df.groupby("Discount_Band", observed=True).agg(
    Avg_Profit=("Profit", "mean"),
    Orders=("Order_ID", "count")
).reset_index()

print("\n💸 DISCOUNT IMPACT ON PROFIT")
print("-" * 40)
print(discount_impact.to_string(index=False))

# ── Export JSON for Dashboard ─────────────────────────────────
output = {
    "kpis": {
        "total_sales": round(total_sales),
        "total_profit": round(total_profit),
        "total_orders": total_orders,
        "avg_discount": round(avg_discount, 1),
        "profit_margin": round(profit_margin, 1)
    },
    "by_category": cat_summary.to_dict(orient="records"),
    "by_region": region_summary.to_dict(orient="records"),
    "monthly_trend": monthly[["Month", "Sales", "Profit"]].to_dict(orient="records"),
    "top_products": top_products.to_dict(orient="records"),
    "discount_impact": discount_impact.to_dict(orient="records")
}

out_path = os.path.join(BASE_DIR, "dashboard", "sales_data.json")
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)

print(f"\n✅ Analysis complete! Data exported → dashboard/sales_data.json")
print("\n" + "=" * 60)
print("  Open dashboard/index.html in your browser to view")
print("  the interactive Sales Performance Dashboard.")
print("=" * 60)
