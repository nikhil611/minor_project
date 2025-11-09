# app.py
import streamlit as st
from rules import get_investment_allocation
from utils import show_header, show_portfolio_chart, card

st.set_page_config(page_title="InvestSmartAI", page_icon="💼", layout="centered")
show_header()

# Sidebar for Inputs
st.sidebar.header("Enter Your Details")
age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=25)
income = st.sidebar.number_input("Monthly Income (₹)", min_value=1000, value=50000)
risk = st.sidebar.selectbox("Risk Appetite", ["Low", "Moderate", "High"])
goal = st.sidebar.selectbox("Investment Goal", ["Short-term", "Long-term", "Retirement", "Wealth Creation"])

if st.sidebar.button("Get Investment Advice"):
    alloc, invest_amt = get_investment_allocation(age, income, risk, goal)

    st.success("✅ Based on your profile, here’s your recommended portfolio:")
    show_portfolio_chart(alloc)

    card("📊 Portfolio Allocation", "<br>".join([f"{k}: {v}%" for k, v in alloc.items()]))
    card("💰 Suggested Monthly Investment", f"₹{invest_amt:,}")
    card("🧩 Advisor’s Note", f"For a **{risk.lower()}** risk profile at age {age}, this mix balances growth and stability toward your **'{goal}'** goal.")
else:
    st.info("👈 Fill out your details on the left and click **Get Investment Advice** to begin.")
